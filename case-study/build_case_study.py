from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Flowable,
)


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output" / "伴读Reader_求职案例.pdf"


def find_font(*candidates):
    for path in candidates:
        if Path(path).exists():
            return path
    raise FileNotFoundError(f"No font found: {candidates}")


CN_FONT = find_font(
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/5f4c23e4a0c7b70597730d79e252955e973ead7d.asset/AssetData/LiHeiPro.ttf",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
)
CN_MEDIUM = find_font(
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
)

try:
    pdfmetrics.registerFont(TTFont("BanduCN", CN_FONT, subfontIndex=0))
    pdfmetrics.registerFont(TTFont("BanduCNMedium", CN_MEDIUM, subfontIndex=0))
except TypeError:
    pdfmetrics.registerFont(TTFont("BanduCN", CN_FONT))
    pdfmetrics.registerFont(TTFont("BanduCNMedium", CN_MEDIUM))


PAGE_W, PAGE_H = A4
INK = colors.HexColor("#193b39")
TEAL = colors.HexColor("#0b7a75")
TEAL_DARK = colors.HexColor("#075e5b")
YELLOW = colors.HexColor("#ffe66d")
CREAM = colors.HexColor("#f6f3ec")
PANEL = colors.HexColor("#fffefa")
MINT = colors.HexColor("#e4f0eb")
LINE = colors.HexColor("#d9d1c3")
MUTED = colors.HexColor("#68736e")
BLUE = colors.HexColor("#1d70b8")
GREEN = colors.HexColor("#147a4b")


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="BodyCN", fontName="BanduCN", fontSize=9.4, leading=14.5,
    textColor=INK, spaceAfter=7, wordWrap="CJK",
))
styles.add(ParagraphStyle(
    name="BodySmall", parent=styles["BodyCN"], fontSize=8.2, leading=12.2,
    textColor=MUTED, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="Hero", fontName="BanduCNMedium", fontSize=29, leading=34,
    textColor=INK, spaceAfter=8, wordWrap="CJK",
))
styles.add(ParagraphStyle(
    name="HeroSub", fontName="BanduCN", fontSize=13, leading=19,
    textColor=TEAL_DARK, spaceAfter=9, wordWrap="CJK",
))
styles.add(ParagraphStyle(
    name="Kicker", fontName="BanduCNMedium", fontSize=8, leading=10,
    textColor=TEAL, spaceAfter=5, wordWrap="CJK",
))
styles.add(ParagraphStyle(
    name="H1CN", fontName="BanduCNMedium", fontSize=17, leading=22,
    textColor=INK, spaceBefore=3, spaceAfter=8, wordWrap="CJK",
))
styles.add(ParagraphStyle(
    name="H2CN", fontName="BanduCNMedium", fontSize=11.2, leading=15,
    textColor=TEAL_DARK, spaceBefore=6, spaceAfter=4, wordWrap="CJK",
))
styles.add(ParagraphStyle(
    name="Meta", fontName="BanduCN", fontSize=8.4, leading=12,
    textColor=MUTED, wordWrap="CJK",
))
styles.add(ParagraphStyle(
    name="MetaStrong", fontName="BanduCNMedium", fontSize=8.4, leading=12,
    textColor=INK, wordWrap="CJK",
))
styles.add(ParagraphStyle(
    name="Callout", fontName="BanduCNMedium", fontSize=14, leading=20,
    textColor=TEAL_DARK, alignment=TA_CENTER, wordWrap="CJK",
))
styles.add(ParagraphStyle(
    name="Quote", fontName="BanduCN", fontSize=10.3, leading=16,
    textColor=TEAL_DARK, leftIndent=10, rightIndent=8, wordWrap="CJK",
))
styles.add(ParagraphStyle(
    name="TableHead", fontName="BanduCNMedium", fontSize=8.3, leading=11,
    textColor=PANEL, wordWrap="CJK",
))
styles.add(ParagraphStyle(
    name="TableBody", fontName="BanduCN", fontSize=8.1, leading=11.5,
    textColor=INK, wordWrap="CJK",
))
styles.add(ParagraphStyle(
    name="TableBodyMuted", fontName="BanduCN", fontSize=8.1, leading=11.5,
    textColor=MUTED, wordWrap="CJK",
))
styles.add(ParagraphStyle(
    name="DiagramLabel", fontName="BanduCNMedium", fontSize=8.2, leading=10,
    textColor=INK, alignment=TA_CENTER, wordWrap="CJK",
))
styles.add(ParagraphStyle(
    name="DiagramSmall", fontName="BanduCN", fontSize=7.2, leading=9,
    textColor=MUTED, alignment=TA_CENTER, wordWrap="CJK",
))


def P(text, style="BodyCN"):
    return Paragraph(text, styles[style])


def bullet(text):
    return P(f"<font color='{TEAL}'>•</font>  {text}", "BodyCN")


class ProductAnatomy(Flowable):
    def __init__(self, width=160 * mm, height=61 * mm):
        super().__init__()
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.setFillColor(PANEL)
        c.setStrokeColor(LINE)
        c.roundRect(0, 0, w, h, 8, fill=1, stroke=1)
        c.setFillColor(CREAM)
        c.roundRect(8, h - 17, w - 16, 10, 4, fill=1, stroke=0)
        c.setFillColor(TEAL)
        c.setFont("BanduCNMedium", 8)
        c.drawString(15, h - 14, "伴读 Reader")
        c.setFillColor(MUTED)
        c.setFont("BanduCN", 6.8)
        c.drawRightString(w - 15, h - 14, "结构提示: 自动    专注阅读: 关")

        c.setFillColor(TEAL)
        c.roundRect(12, h - 34, 45, 10, 4, fill=1, stroke=0)
        c.setFillColor(PANEL)
        c.setFont("BanduCNMedium", 6.5)
        c.drawCentredString(34.5, h - 31, "开始伴读")

        c.setFillColor(INK)
        c.setFont("BanduCN", 9.2)
        lines = [
            "When you give a coding assistant a task, it follows a process",
            "similar to how a human developer would approach the problem.",
            "The current word becomes a small, calm place to return to.",
        ]
        y = h - 50
        for i, line in enumerate(lines):
            c.drawString(16, y - i * 12, line)
        c.setFillColor(YELLOW)
        c.roundRect(259, h - 51, 30, 12, 3, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont("BanduCNMedium", 8.2)
        c.drawString(264, h - 48, "word")
        c.setStrokeColor(BLUE)
        c.setLineWidth(1.1)
        c.line(16, 9, 74, 9)
        c.setStrokeColor(GREEN)
        c.setDash(2, 2)
        c.line(91, 9, 160, 9)
        c.setDash()
        c.setFillColor(MUTED)
        c.setFont("BanduCN", 6.6)
        c.drawString(176, 6.5, "结构线索")
        c.setFillColor(TEAL)
        c.setFont("BanduCNMedium", 7.5)
        c.drawRightString(w - 16, 8, "只让注意力有一个落点")


class ProcessDiagram(Flowable):
    def __init__(self, width=160 * mm, height=45 * mm):
        super().__init__()
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        labels = [
            ("进入", "Enter", "降低开始阻力", CREAM),
            ("看见", "Notice", "给注意力落点", MINT),
            ("留下", "Leave traces", "保留自己的判断", colors.HexColor("#fff3bf")),
            ("返回", "Return", "支持第二遍和第 N 遍", colors.HexColor("#e4edf5")),
        ]
        gap = 9
        box_w = (w - gap * 3) / 4
        y = 11
        for i, (cn, en, desc, fill) in enumerate(labels):
            x = i * (box_w + gap)
            c.setFillColor(fill)
            c.setStrokeColor(LINE)
            c.roundRect(x, y, box_w, h - 20, 7, fill=1, stroke=1)
            c.setFillColor(INK)
            c.setFont("BanduCNMedium", 11)
            c.drawCentredString(x + box_w / 2, h - 23, cn)
            c.setFillColor(TEAL_DARK)
            c.setFont("Helvetica-Bold", 7.5)
            c.drawCentredString(x + box_w / 2, h - 34, en)
            c.setFillColor(MUTED)
            c.setFont("BanduCN", 7)
            c.drawCentredString(x + box_w / 2, h - 47, desc)
            if i < 3:
                c.setStrokeColor(TEAL)
                c.setLineWidth(1.2)
                c.line(x + box_w + 2, h / 2, x + box_w + gap - 2, h / 2)
                c.line(x + box_w + gap - 5, h / 2 + 2.3, x + box_w + gap - 2, h / 2)
                c.line(x + box_w + gap - 5, h / 2 - 2.3, x + box_w + gap - 2, h / 2)


class AttentionLayers(Flowable):
    def __init__(self, width=160 * mm, height=41 * mm):
        super().__init__()
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        rows = [
            ("原文", "保留段落、换行和完整语境", PANEL, INK),
            ("结构", "下划线、点线和少量色块表达关系", colors.HexColor("#e7f0f6"), BLUE),
            ("当前词", "黄色高亮，朗读与视觉同步", colors.HexColor("#fff3a6"), INK),
            ("专注阅读", "需要时才让当前句站出来", colors.HexColor("#dceee8"), TEAL_DARK),
        ]
        row_h = (h - 9) / 4
        for i, (label, desc, fill, text_color) in enumerate(rows):
            y = h - (i + 1) * row_h - i * 3
            c.setFillColor(fill)
            c.setStrokeColor(LINE)
            c.roundRect(0, y, w, row_h, 5, fill=1, stroke=1)
            c.setFillColor(text_color)
            c.setFont("BanduCNMedium", 8.4)
            c.drawString(10, y + row_h / 2 + 2, label)
            c.setFillColor(MUTED)
            c.setFont("BanduCN", 7.6)
            c.drawString(62, y + row_h / 2 + 2, desc)


def meta_box(label, value):
    return Table(
        [[P(label, "Meta"), P(value, "MetaStrong")]],
        colWidths=[25 * mm, 49 * mm],
        style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), PANEL),
            ("BOX", (0, 0), (-1, -1), 0.6, LINE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]),
    )


def callout(text, fill=MINT):
    return Table([[P(text, "Callout")]], colWidths=[160 * mm], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), fill),
        ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#b7d4c9")),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 11),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
    ]))


def draw_page(c, doc):
    c.saveState()
    c.setFillColor(CREAM)
    c.rect(0, PAGE_H - 14 * mm, PAGE_W, 14 * mm, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.rect(0, PAGE_H - 14 * mm, 12 * mm, 14 * mm, fill=1, stroke=0)
    c.setFillColor(MUTED)
    c.setFont("Helvetica-Bold", 7.4)
    c.drawString(18 * mm, PAGE_H - 8.5 * mm, "BANDU READER  /  PRODUCT CASE STUDY")
    c.drawRightString(PAGE_W - 16 * mm, 10 * mm, f"{doc.page:02d}  /  04")
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(16 * mm, 14 * mm, PAGE_W - 16 * mm, 14 * mm)
    c.restoreState()


def build_story():
    story = []

    # Page 1: framing
    story += [Spacer(1, 12 * mm), P("产品案例 / PRODUCT CASE", "Kicker")]
    story += [P("伴读 Reader", "Hero")]
    story += [P("为长文、学习材料和严肃内容设计的低阻力阅读辅助", "HeroSub")]
    story += [P("A local-first reading scaffold for people who want reading to feel safer, clearer, and easier to return to.", "BodySmall")]
    story += [Spacer(1, 3 * mm), ProductAnatomy(), Spacer(1, 6 * mm)]
    meta = Table([[meta_box("角色", "独立产品项目"), meta_box("范围", "产品 / UX / 前端")],
                 [meta_box("平台", "Responsive web"), meta_box("状态", "已发布可用原型")]], colWidths=[78 * mm, 78 * mm], hAlign="LEFT")
    meta.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 4), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    story += [meta, Spacer(1, 7 * mm)]
    story += [P("01  问题：不是不想读，而是很难进入", "H1CN")]
    story += [P("面对论文、课程材料、长邮件或专业文档时，阻力往往发生在真正理解之前：整屏文字带来过载，注意力容易漂移，朗读和高亮不一定同步，读到一半后很难返回重点。长期的失败体验还会叠加羞耻和自我否定。", "BodyCN")]
    story += [P("我希望做的不是一个替用户总结的工具，而是一个让人可以一次次回到原文的阅读脚手架。", "BodyCN")]
    story += [callout("让阅读更容易开始，也更容易继续。<br/><font name='Helvetica' size='9'>Make reading easier to start, and easier to keep going.</font>", colors.HexColor("#e3f1ed")), Spacer(1, 5 * mm)]
    story += [P("设计约束", "H2CN")]
    story += [bullet("本地优先: 不登录、不上传文字、不接入在线 AI"), bullet("不抢走学习过程: 不用自动总结替代用户理解"), bullet("低启动成本: 打开网页、粘贴文字、马上开始"), bullet("Every feature must earn its weight.")]
    story.append(PageBreak())

    # Page 2: product logic
    story += [Spacer(1, 8 * mm), P("02  产品逻辑：进入、看见、留下、返回", "H1CN")]
    story += [P("我把阅读过程拆成四个连续动作，而不是把功能堆在同一层界面里。", "BodyCN"), Spacer(1, 2 * mm), ProcessDiagram(), Spacer(1, 5 * mm)]
    story += [P("这些机制共同服务一个目标: 让用户保留自己的理解，而不是获得一个看似完成的结果。", "Quote"), Spacer(1, 5 * mm)]
    story += [P("关键设计决策", "H1CN")]
    story += [P("让注意力有落点，但不制造新的噪音", "H2CN")]
    story += [bullet("普通模式只突出当前词，结构提示使用下划线、点线和少量色块表达关系"), bullet("专注阅读才突出整句，周围内容退后，当前词继续移动"), bullet("结构提示默认自动适配中英文: 中文侧重逻辑信号和概念复现，英文侧重信息流"), bullet("英文词首加粗默认开启，但作为低强度视觉引导，设置里可关闭")]
    story += [Spacer(1, 3 * mm), AttentionLayers(), Spacer(1, 4 * mm)]
    story += [P("让控制权跟着阅读动作走", "H2CN")]
    story += [bullet("暂停和继续是同一个动作；暂停后可以上一句 / 下一句，不必从头播放"), bullet("速度在阅读中也可以调整，并在继续时生效"), bullet("标记动作放在专注阅读的当前句旁；停止后收起输入区和设置，让页面回到自由浏览状态")]
    story.append(PageBreak())

    # Page 3: iteration
    story += [Spacer(1, 8 * mm), P("03  迭代：从真实阻力反推产品", "H1CN")]
    story += [P("这个项目不是一次性完成的页面，而是通过持续使用和反馈逐步收敛。每一轮都问同一个问题: 它是在帮助用户回到阅读，还是把用户带离阅读?", "BodyCN")]
    rows = [
        [P("观察到的阻力", "TableHead"), P("设计回应", "TableHead")],
        [P("一整段高亮让人不知道当前读到哪里", "TableBody"), P("改为逐词高亮，并加入朗读与视觉推进同步", "TableBodyMuted")],
        [P("长文本朗读中途漏读、读完一小段就结束", "TableBody"), P("按句子和短块切分语音，继续时从当前位置接着走", "TableBodyMuted")],
        [P("语速、暂停、继续的语义不清", "TableBody"), P("统一暂停 / 继续，支持阅读中调整速度并保留偏好", "TableBodyMuted")],
        [P("专注阅读里整句绿色背景随每个词闪动", "TableBody"), P("取消整句动画，只保留当前词的轻微出现效果", "TableBodyMuted")],
        [P("结构提示和当前句整块背景叠加，视觉过载", "TableBody"), P("普通模式取消整句背景，结构提示只表达关系", "TableBodyMuted")],
        [P("新用户可能永远发现不了专注阅读", "TableBody"), P("第一次放入较长文本时轻量询问是否体验", "TableBodyMuted")],
        [P("顶部按钮越来越多", "TableBody"), P("将主要动作、阅读控制和低频设置分层，并持续做减法", "TableBodyMuted")],
    ]
    table = Table(rows, colWidths=[67 * mm, 93 * mm], repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TEAL_DARK),
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [PANEL, colors.HexColor("#faf8f2")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story += [table, Spacer(1, 7 * mm)]
    story += [P("从功能到系统", "H2CN")]
    story += [P("最初的需求看起来像“朗读 + 高亮 + Bionic Reading”，但实际使用后，真正重要的是状态之间的关系: 读到哪里、如何回来、什么时候减少信息、哪些痕迹值得留下。因此产品逐渐从一组效果，变成了一个有层次的阅读系统。", "BodyCN")]
    story += [callout("减法不是把功能做少，而是让每个功能只在它真正有帮助的时刻出现。", colors.HexColor("#fff5ce"))]
    story.append(PageBreak())

    # Page 4: outcome and reflection
    story += [Spacer(1, 8 * mm), P("04  结果、边界与下一步", "H1CN")]
    story += [P("已交付", "H2CN")]
    story += [bullet("可在 Windows、Mac 和移动浏览器使用的响应式网页原型"), bullet("GitHub Pages 在线版，无需安装、注册或登录"), bullet("中文 / English 界面，浏览器语言自动识别，也保留手动切换"), bullet("浏览器系统语音、当前词高亮、专注阅读、结构提示和本地回看线索"), bullet("保留原文段落与换行，支持从第一遍阅读到第 N 遍回看")]
    story += [Spacer(1, 3 * mm), P("我学到的", "H2CN")]
    story += [P("辅助阅读产品的“温柔”不主要来自鼓励文案，而来自结构: 更少的选择、更清楚的当前状态、更容易回到上一步，以及不把用户的困难解释成能力不足。", "BodyCN")]
    story += [P("这也改变了我对产品成功的判断。它不需要让用户看起来更高效，而要让用户更愿意再次打开文本，继续形成自己的理解。", "BodyCN")]
    story += [Spacer(1, 2 * mm), P("诚实的边界", "H2CN")]
    story += [bullet("系统语音质量因设备而异，朗读和高亮仍可能有轻微时差"), bullet("结构提示是启发式线索，不是语义真理"), bullet("PDF / OCR 尚未进入核心流程，也还没有正式的长期用户研究"), bullet("下一步先做小规模可用性测试，观察不同阅读者能否更顺利开始、回来和坚持")]
    story += [Spacer(1, 5 * mm), callout("The product is not a finished answer. It is a gentler doorway back to the text.", colors.HexColor("#e3f1ed")), Spacer(1, 6 * mm)]
    links = Table([
        [P("在线版", "Meta"), P("sheahe-alex.github.io/slowglow-reader/", "MetaStrong")],
        [P("代码仓库", "Meta"), P("github.com/sheahe-Alex/slowglow-reader", "MetaStrong")],
        [P("我负责", "Meta"), P("产品定义、交互设计、前端实现、双语文案、迭代验证", "MetaStrong")],
    ], colWidths=[26 * mm, 134 * mm])
    links.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PANEL),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(links)
    return story


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(OUT), pagesize=A4,
        leftMargin=25 * mm, rightMargin=25 * mm,
        topMargin=21 * mm, bottomMargin=21 * mm,
        title="伴读 Reader 求职案例",
        author="伴读 Reader",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body")
    doc.addPageTemplates([PageTemplate(id="case", frames=[frame], onPage=draw_page)])
    doc.build(build_story())
    print(OUT)


if __name__ == "__main__":
    main()
