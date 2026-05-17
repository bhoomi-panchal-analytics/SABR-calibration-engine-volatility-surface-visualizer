from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_report(
    filename,
    title="SABR Quant Research Report"
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title_paragraph = Paragraph(
        title,
        styles['Title']
    )

    elements.append(title_paragraph)

    elements.append(Spacer(1, 20))

    intro = Paragraph(
        """
        This report summarizes:
        <br/><br/>
        • SABR calibration<br/>
        • Volatility surface analysis<br/>
        • Greeks exposure<br/>
        • Arbitrage diagnostics<br/>
        • Monte Carlo simulation results
        """,
        styles['BodyText']
    )

    elements.append(intro)

    doc.build(elements)
