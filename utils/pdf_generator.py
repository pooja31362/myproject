from fpdf import FPDF
import os

def generate_invoice_pdf(booking, booking_id):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Hotel Booking Invoice", ln=True, align="C")
        pdf.ln(10)

        pdf.set_text_color(0, 0, 0)
        pdf.cell(200, 10, txt=f"Booking ID: {booking_id}", ln=True)
        pdf.cell(200, 10, txt=f"Customer: {booking['name']}", ln=True)
        pdf.cell(200, 10, txt=f"Email: {booking['email']}", ln=True)
        pdf.cell(200, 10, txt=f"Phone: {booking['phone']}", ln=True)
        pdf.cell(200, 10, txt=f"Govt ID: {booking['govt_id']}", ln=True)
        pdf.cell(200, 10, txt=f"Hotel: {booking['hotel_name']}", ln=True)
        pdf.cell(200, 10, txt=f"Location: {booking['location']}", ln=True)
        pdf.cell(200, 10, txt=f"Rating: {'★' * booking.get('rating', 4)}", ln=True)  # 4 stars default
        pdf.cell(200, 10, txt=f"Guests: {booking['guest_count']}", ln=True)
        pdf.cell(200, 10, txt=f"Check-in: {booking['checkin']}", ln=True)
        pdf.cell(200, 10, txt=f"Check-out: {booking['checkout']}", ln=True)

        if booking.get("features"):
            pdf.cell(200, 10, txt=f"Access Chosen: {booking['features']}", ln=True)

        pdf.ln(10)
        pdf.cell(200, 10, txt="--- Billing Summary ---", ln=True)
        pdf.cell(200, 10, txt=f"Room Total: ₹{booking['room_total']}", ln=True)
        pdf.cell(200, 10, txt=f"Meal Total: ₹{booking['meal_total']}", ln=True)
        pdf.cell(200, 10, txt=f"Discount: ₹{booking['discount']}", ln=True)
        pdf.cell(200, 10, txt=f"GST (18%): ₹{booking['gst']}", ln=True)
        pdf.cell(200, 10, txt=f"Grand Total: ₹{booking['grand_total']}", ln=True)

        # Save
        pdf_dir = "invoices"
        if not os.path.exists(pdf_dir):
            os.makedirs(pdf_dir)
        pdf_path = os.path.join(pdf_dir, f"invoice_{booking_id}.pdf")
        pdf.output(pdf_path)

        return pdf_path if os.path.exists(pdf_path) else None
    except Exception as e:
        print(f"PDF generation error for booking ID {booking_id}: {e}")
        return None
