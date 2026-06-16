from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Table


def generate_invoice(
    bill_no,
    invoice_rows,
    grand_total
):

    filename = f"bills/{bill_no}.pdf"

    # Dynamic height based on number of products
    height = max(
        100,
        60 + len(invoice_rows) * 10
    )

    doc = SimpleDocTemplate(
        filename,
        pagesize=(80 * mm, height * mm),
        leftMargin=5,
        rightMargin=5,
        topMargin=5,
        bottomMargin=5
    )

    styles = getSampleStyleSheet()

    # Smaller fonts for receipt style
    styles["Title"].fontSize = 14
    styles["Heading2"].fontSize = 10
    styles["Normal"].fontSize = 8

    elements = []

    elements.append(
        Paragraph(
            "Inventra",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            f"Bill No: {bill_no}",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 5)
    )

    data = [
    ["Product", "Qty", "Total"]
    ]
    
    for row in invoice_rows:
        data.append([
            row["Product"],
            row["Qty"],
            row["Total"]
        ])
    
    table = Table(
        data,
        colWidths=[40*mm, 15*mm, 15*mm]
    )
    
    elements.append(table)

    elements.append(
        Spacer(1, 5)
    )

    elements.append(
        Paragraph(
            f"Grand Total: Rs {grand_total}",
            styles["Heading2"]
        )
    )

    doc.build(elements)

    return filename