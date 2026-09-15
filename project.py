import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import random
import os

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jam3eya.db")


# ======================================================
#  طبقة قاعدة البيانات
# ======================================================
class Database:
    """كل التعامل مع SQLite بمكان واحد حتى يسهل التعديل عليه."""

    def __init__(self, db_path=DB_FILE):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self._create_tables()

    def _create_tables(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                key   TEXT PRIMARY KEY,
                value TEXT
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS members (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                name        TEXT NOT NULL,
                phone       TEXT,
                shares      INTEGER NOT NULL,
                turn_order  INTEGER,
                received    INTEGER NOT NULL DEFAULT 0
            )
        """)
        self.conn.commit()

    # ---------- الإعدادات (سعر السهم) ----------
    def get_setting(self, key, default=None):
        cur = self.conn.execute("SELECT value FROM settings WHERE key = ?", (key,))
        row = cur.fetchone()
        return row[0] if row else default

    def set_setting(self, key, value):
        self.conn.execute(
            "INSERT INTO settings (key, value) VALUES (?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
            (key, str(value))
        )
        self.conn.commit()

    # ---------- الأعضاء ----------
    def add_member(self, name, phone, shares):
        self.conn.execute(
            "INSERT INTO members (name, phone, shares) VALUES (?, ?, ?)",
            (name, phone, shares)
        )
        self.conn.commit()

    def delete_member(self, member_id):
        self.conn.execute("DELETE FROM members WHERE id = ?", (member_id,))
        self.conn.commit()

    def get_all_members(self):
        cur = self.conn.execute(
            "SELECT id, name, phone, shares, turn_order, received "
            "FROM members ORDER BY (turn_order IS NULL), turn_order, id"
        )
        return cur.fetchall()

    def set_turn_order(self, member_id, order):
        self.conn.execute(
            "UPDATE members SET turn_order = ?, received = 0 WHERE id = ?",
            (order, member_id)
        )
        self.conn.commit()

    def mark_received(self, member_id):   # بميز اللي استلم 
        self.conn.execute("UPDATE members SET received = 1 WHERE id = ?", (member_id,))
        self.conn.commit()

    def reset_round(self):     # بس تنتهي الجمعيه بالكامل الكل برجع لحاله عدم الاستلام في حال بدهم يعيدوها
        self.conn.execute("UPDATE members SET received = 0")
        self.conn.commit()

    def close(self):
        self.conn.close()


# ======================================================
#  الألوان والخطوط (لمكان واحد يسهل التعديل عليه)
# ======================================================
COLOR_BG        = "#eef2f5"
COLOR_HEADER    = "#1f2d3d"
COLOR_HEADER_TX = "#ffffff"
COLOR_ACCENT    = "#178a6b"
COLOR_ACCENT_TX = "#ffffff"
COLOR_CARD      = "#ffffff"
COLOR_BORDER    = "#d7dde2"
COLOR_TEXT      = "#2c3e50"
COLOR_MUTED     = "#7f8c8d"
COLOR_DANGER    = "#c0392b"
COLOR_OK        = "#178a6b"

FONT_TITLE  = ("Segoe UI", 16, "bold")
FONT_H2     = ("Segoe UI", 12, "bold")
FONT_BASE   = ("Segoe UI", 10)
FONT_BOLD   = ("Segoe UI", 10, "bold")
FONT_SMALL  = ("Segoe UI", 9)


# ======================================================
#  التطبيق الرئيسي
# ======================================================
class Jam3eyaApp:
    def __init__(self, root):
        self.root = root
        self.db = Database()

        self.root.title("جمعية ام محمد وجاراتها")
        self.root.geometry("780x620")
        self.root.minsize(720, 560)    # الحجم الاصلي للنافذه واللي ما بقدر اصغر منو 
        self.root.configure(bg=COLOR_BG)

        self.share_price = float(self.db.get_setting("share_price", 0) or 0)    # سعر السهم الافتراضي

        self._build_style()
        self._build_header()
        self._build_share_price_card()
        self._build_add_member_card()
        self._build_table_card()
        self._build_status_bar()

        self.refresh_table()

    # -------------------------------------------------
    #  الأنماط (ttk)
    # -------------------------------------------------
    def _build_style(self):
        style = ttk.Style() # ttk النمط المستخدم للنافذه بشكل افضل من tkinter
        style.theme_use("clam")

        style.configure("Treeview", rowheight=30, font=FONT_BASE, # لعمل مساحه القائمه المنسدله
                         background=COLOR_CARD, fieldbackground=COLOR_CARD,
                         borderwidth=0)
        style.configure("Treeview.Heading", font=FONT_BOLD,
                         background="#f1f4f6", foreground=COLOR_TEXT, relief="flat")
        style.map("Treeview", background=[("selected", COLOR_ACCENT)],
                  foreground=[("selected", "white")])

        style.configure("Accent.TButton", font=FONT_BOLD, padding=8,
                         background=COLOR_ACCENT, foreground=COLOR_ACCENT_TX)
        style.map("Accent.TButton", background=[("active", "#136f56")])

        style.configure("Flat.TButton", font=FONT_BASE, padding=7,
                         background="#e4e9ec", foreground=COLOR_TEXT)
        style.map("Flat.TButton", background=[("active", "#d3dadf")])

        style.configure("Danger.TButton", font=FONT_BASE, padding=7,
                         background="#f5d7d3", foreground=COLOR_DANGER)
        style.map("Danger.TButton", background=[("active", "#eec1bb")])

        style.configure("TEntry", padding=5)

    # -------------------------------------------------
    #  الهيدر العلوي
    # -------------------------------------------------
    def _build_header(self):
        header = tk.Frame(self.root, bg=COLOR_HEADER, height=64)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(header, text="جمعية ام محمد وجاراتها", font=FONT_TITLE,
                 bg=COLOR_HEADER, fg=COLOR_HEADER_TX).pack(side="right", padx=20)

        tk.Label(header, text="تطوير  : ", font=FONT_SMALL,
                 bg=COLOR_HEADER, fg="#9aa7b4").pack(side="left", padx=(20, 2), pady=20)
        tk.Label(header, text="osama nemrawi", font=("Segoe UI", 9, "bold"),
                 bg=COLOR_HEADER, fg="#ecf0f1").pack(side="left", pady=20)

    # -------------------------------------------------
    #  بطاقة سعر السهم
    # -------------------------------------------------
    def _build_share_price_card(self):
        card = self._make_card()

        tk.Label(card, text="سعر السهم", font=FONT_H2,
                 bg=COLOR_CARD, fg=COLOR_TEXT).grid(row=0, column=3, sticky="e", padx=5, pady=(0, 8))

        row = tk.Frame(card, bg=COLOR_CARD)
        row.grid(row=1, column=0, columnspan=4, sticky="we")

        self.share_price_entry = ttk.Entry(row, width=14, justify="center")
        self.share_price_entry.pack(side="right", padx=(0, 8))
        if self.share_price > 0:
            self.share_price_entry.insert(0, f"{self.share_price:g}")

        ttk.Button(row, text="تثبيت السعر", style="Accent.TButton",
                   command=self.set_share_price).pack(side="right", padx=(0, 8))

        self.share_price_label = tk.Label(
            row, font=FONT_SMALL, bg=COLOR_CARD,
            text=self._share_price_text(), fg=self._share_price_color()
        )
        self.share_price_label.pack(side="left")

    def _share_price_text(self):
        if self.share_price > 0:
            return f"✔ السعر الحالي: {self.share_price:g}"
        return "لم يتم تحديد سعر السهم بعد"

    def _share_price_color(self):
        return COLOR_OK if self.share_price > 0 else COLOR_DANGER

    def set_share_price(self):
        value = self.share_price_entry.get().strip()
        try:
            price = float(value)
            if price <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("خطأ", "الرجاء إدخال سعر سهم صحيح (رقم أكبر من صفر).")
            return

        self.share_price = price
        self.db.set_setting("share_price", price)

        self.share_price_label.config(text=self._share_price_text(),
                                       fg=self._share_price_color())
        self.refresh_table()

    # -------------------------------------------------
    #  بطاقة إضافة عضو
    # -------------------------------------------------
    def _build_add_member_card(self):
        card = self._make_card()

        tk.Label(card, text="إضافة مشترك جديد", font=FONT_H2,
                 bg=COLOR_CARD, fg=COLOR_TEXT).grid(row=0, column=0, columnspan=4,
                                                     sticky="e", pady=(0, 10))

        tk.Label(card, text="الاسم", font=FONT_SMALL, bg=COLOR_CARD,
                 fg=COLOR_MUTED).grid(row=1, column=3, sticky="e", padx=5)
        self.name_entry = ttk.Entry(card, width=20)
        self.name_entry.grid(row=2, column=3, sticky="e", padx=5)

        tk.Label(card, text="رقم الهاتف", font=FONT_SMALL, bg=COLOR_CARD,
                 fg=COLOR_MUTED).grid(row=1, column=2, sticky="e", padx=5)
        self.phone_entry = ttk.Entry(card, width=16)
        self.phone_entry.grid(row=2, column=2, sticky="e", padx=5)

        tk.Label(card, text="عدد الأسهم", font=FONT_SMALL, bg=COLOR_CARD,
                 fg=COLOR_MUTED).grid(row=1, column=1, sticky="e", padx=5)
        self.shares_entry = ttk.Entry(card, width=10)
        self.shares_entry.grid(row=2, column=1, sticky="e", padx=5)

        ttk.Button(card, text="➕ إضافة", style="Accent.TButton",
                   command=self.add_member).grid(row=2, column=0, sticky="w", padx=5)

    # -------------------------------------------------
    #  بطاقة الجدول والأزرار
    # -------------------------------------------------
    def _build_table_card(self):
        outer = tk.Frame(self.root, bg=COLOR_BG, padx=18)
        outer.pack(fill="both", expand=True, pady=(4, 4))

        card = tk.Frame(outer, bg=COLOR_CARD, highlightbackground=COLOR_BORDER,
                         highlightthickness=1)
        card.pack(fill="both", expand=True)

        table_frame = tk.Frame(card, bg=COLOR_CARD)
        table_frame.pack(fill="both", expand=True, padx=12, pady=12)

        columns = ("order", "name", "phone", "shares", "amount", "status")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

        headers = {
            "order": "الدور", "name": "الاسم", "phone": "الهاتف",
            "shares": "الأسهم", "amount": "قيمة الاشتراك", "status": "الحالة",
        }
        widths = {"order": 55, "name": 160, "phone": 110, "shares": 70,
                   "amount": 120, "status": 110}

        for col in columns:
            self.tree.heading(col, text=headers[col])
            self.tree.column(col, width=widths[col], anchor="center")

        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        btns = tk.Frame(outer, bg=COLOR_BG, pady=10)
        btns.pack(fill="x")

        ttk.Button(btns, text="🎲 إجراء القرعة", style="Accent.TButton",
                   command=self.run_draw).pack(side="right", padx=4)
        ttk.Button(btns, text="✔ تمييز كمستلم", style="Flat.TButton",
                   command=self.mark_received).pack(side="right", padx=4)
        ttk.Button(btns, text="↺ جولة جديدة", style="Flat.TButton",
                   command=self.reset_round).pack(side="right", padx=4)
        ttk.Button(btns, text="🗑 حذف المشترك", style="Danger.TButton",
                   command=self.delete_member).pack(side="right", padx=4)

    # -------------------------------------------------
    #  شريط الحالة السفلي
    # -------------------------------------------------
    def _build_status_bar(self):
        self.status_label = tk.Label(
            self.root, text="", bg=COLOR_HEADER, fg="#ecf0f1",
            font=FONT_SMALL, anchor="w", padx=18, pady=8
        )
        self.status_label.pack(fill="x", side="bottom")

    # -------------------------------------------------
    #  أداة مساعدة لإنشاء بطاقة موحدة الشكل
    # -------------------------------------------------
    def _make_card(self):
        outer = tk.Frame(self.root, bg=COLOR_BG, padx=18, pady=8)
        outer.pack(fill="x")

        card = tk.Frame(outer, bg=COLOR_CARD, highlightbackground=COLOR_BORDER,
                         highlightthickness=1, padx=14, pady=12)
        card.pack(fill="x")
        card.columnconfigure(3, weight=1)
        return card

    # -------------------------------------------------
    #  منطق العمل (يستخدم Database فقط، بلا حسابات يدوية)
    # -------------------------------------------------
    def add_member(self):
        if self.share_price <= 0:
            messagebox.showwarning("تنبيه", "الرجاء تثبيت سعر السهم أولاً قبل إضافة المشتركين.")
            return

        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        shares = self.shares_entry.get().strip()

        if not name or not phone or not shares:
            messagebox.showwarning("تنبيه", "الرجاء تعبئة جميع الخانات (الاسم، رقم الهاتف، وعدد الأسهم).")
            return 
        try:
            shares_val = int(shares)
            if shares_val <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("خطأ", "عدد الأسهم يجب أن يكون رقماً صحيحاً أكبر من صفر.")
            return

        # --- بداية التعديل الذكي لمنع تصفير القرعة القديمة ---
        members = self.db.get_all_members()
        
        # نتحقق: هل هناك قرعة قائمة فعلياً بالبرنامج؟
        has_draw = any(m[4] is not None for m in members)
        
        # إضافة العضو الجديد لقاعدة البيانات بشكل عادي أولاً
        self.db.add_member(name, phone, shares_val)
        
        if has_draw:
            # نجلب أرقام الأدوار الحالية للأعضاء المشاركين بالقرعة
            existing_orders = [m[4] for m in members if m[4] is not None]
            # نحدد من هو صاحب الرقم الأخير (أكبر رقم دور)
            max_order = max(existing_orders) if existing_orders else 0
            
            # نجلب المشترك الجديد الذي تمت إضافته للتو (صاحب أكبر ID في قاعدة البيانات)
            all_members_now = self.db.get_all_members()
            new_member = max(all_members_now, key=lambda m: m[0])
            
            # نثبت دور العضو الجديد ليكون (آخر دور + 1) دون التأثير على البقية
            self.db.set_turn_order(new_member[0], max_order + 1)
            
            messagebox.showinfo("تمت الإضافة", f"تمت إضافة {name} وحجز آخر دور له بالقرعة تلقائياً (الدور رقم {max_order + 1}) 🎉")
        # ----------------------------------------------------

        # تفريغ حقول الكتابة لاستقبال عضو جديد
        self.name_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.shares_entry.delete(0, "end")

        self.refresh_table()
    def delete_member(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("تنبيه", "الرجاء اختيار مشترك لحذفه.")
            return

        member_id = int(selected[0])
        self.db.delete_member(member_id)
        self.db.clear_all_orders()  # حذف عضو يفرض إعادة القرعة

        self.refresh_table()

    def run_draw(self):
        members = self.db.get_all_members()
        if len(members) < 2:
            messagebox.showinfo("تنبيه", "لازم يكون في مشتركَين على الأقل لإجراء القرعة.")
            return

        confirm = messagebox.askyesno("تأكيد القرعة",
                                       "هل تريد إجراء قرعة عشوائية لتوزيع أدوار الاستلام؟")
        if not confirm:
            return

        ids = [m[0] for m in members]
        random.shuffle(ids)
        for order, member_id in enumerate(ids, start=1):
            self.db.set_turn_order(member_id, order)

        self.refresh_table()
        messagebox.showinfo("تمت القرعة", "تم توزيع أدوار الاستلام عشوائياً بنجاح 🎉")

    def mark_received(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("تنبيه", "الرجاء اختيار مشترك لتمييزه كمستلم.")
            return

        member_id = int(selected[0])
        member = next((m for m in self.db.get_all_members() if m[0] == member_id), None)
        if member and member[4] is None:
            messagebox.showwarning("تنبيه", "لازم تعمل القرعة أولاً قبل تمييز الاستلام.")
            return

        self.db.mark_received(member_id)
        self.refresh_table()

    def reset_round(self):
        confirm = messagebox.askyesno(
            "تأكيد", "هل تريد بدء جولة جديدة؟ سيتم تصفير حالة الاستلام للجميع (بنفس ترتيب القرعة الحالي)."
        )
        if confirm:
            self.db.reset_round()
            self.refresh_table()

    # -------------------------------------------------
    #  تحديث الجدول وشريط الحالة من قاعدة البيانات مباشرة
    # -------------------------------------------------
    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        members = self.db.get_all_members()
        for member_id, name, phone, shares, order, received in members:
            order_text = order if order is not None else "—"
            status = "✔ استلم" if received else "بالانتظار"
            amount = shares * self.share_price
            self.tree.insert("", "end", iid=str(member_id), values=(
                order_text, name, phone or "-", shares, f"{amount:.2f}", status
            ))

        self._update_status(members)

    def _update_status(self, members):
        total_members = len(members)
        total_shares = sum(m[3] for m in members)
        total_amount = total_shares * self.share_price
        draw_done = total_members > 0 and all(m[4] is not None for m in members)

        if not draw_done:
            next_text = "لم تتم القرعة بعد"
        else:
            pending = sorted([m for m in members if not m[5]], key=lambda m: m[4])
            next_text = f"الدور القادم: {pending[0][1]}" if pending else "جميع المشتركين استلموا دورهم 🎉"

        self.status_label.config(
            text=(f"عدد المشتركين: {total_members}    |    إجمالي الأسهم: {total_shares}    |    "
                  f"إجمالي الجمعية: {total_amount:.2f}    |    {next_text}")
        )

    def on_close(self):
        self.db.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Jam3eyaApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()