import datetime
import smtplib
from flask import Flask
app = Flask(__name__)

pricing_map = {}
pricing_map["Audio Glass"] = 249.99
pricing_map["Audio Glasses"] = 249.99
pricing_map["Insurance"] = 50
pricing_map["Speaker"] = 50
pricing_map["Speakers"] = 50
pricing_map["Headphones"] = 20
pricing_map["Headphone"] = 20
pricing_map["Sunglasses"] = 50

def get_price(product):
    toSearch = product
    if "(" in product:
        toSearch = product.split("(")[0]
    return pricing_map[toSearch]

def get_all_product_price(product_list):
    total_price = 0
    for product in product_list:
        total_price = total_price + product[0] * get_price(product[1])
    return round(total_price, 2)

def generate_email_body(place, name, company, school, email, product_list):
    email_body = "Hi " + name + ", " + "\n\n" + \
                 "This is Virtual Enterprise company Audio Glass. " + \
                 "You have made a purchase from our company at the " + place + " trade show. The following is your order: \n\n"

    product_table = "{0:20} | {1:20} | {2:15} | {3:15} \n".format("Quatity", "Product", "Unit Price", "Total Price")
    for product in product_list:
        product_table = product_table + "{0:20} | {1:20} | {2:15} | {3:15} \n".format(str(product[0]), product[1], str(get_price(product[1])), str(get_price(product[1]) * product[0]))

    product_table = product_table + "{0:10} {1:20} {2:15} {3:15} \n".format("Tax", "", "", str(round(get_all_product_price(product_list) * 0.08), 2))
    email_body = email_body + product_table + "\n"
    email_body = email_body + \
                 "The total amount of your order is $" + str(round(get_all_product_price(product_list) * 1.08, 2)) + ". Please make your payment within 30 days. Thank you so much for the business. We hope to see you again! \n\n" + \
                 "Audio Glass Sales Department \n" + datetime.date.today().strftime("%B %d, %Y")
    return email_body

def send_email(email, email_body):
    gmail_user = 'audioglass0@gmail.com'
    gmail_password = 'paulgeorgePG13'

    sent_from = gmail_user
    to = [email]
    subject = 'Audio Glass Sales Order'
    body = email_body

    email_text = """\ 
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    msg = "\r\n".join([
        "From: " + sent_from,
        "To: " + ", ".join(to),
        "Subject: " + subject,
        "",
        body
    ])

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, msg)
        server.close()
        print('Email sent!')

    except:
        print('Something went wrong...')

def process_and_email(place, name, company, school, email, product_list):
    email_body = generate_email_body(place, name, company, school, email, product_list)
    print(email_body)
    send_email(email, email_body)
    total_price = get_all_product_price(product_list) * 1.08
    return round(total_price, 2)


#process_and_email("San Diego", "Howard Li", "Audio Glasses Inc.", "Univ HS", "lihoward07@gmail.com", product_list)

@app.route("/order/<name>/<company>/<school>/<email>/<order>")
def make_order(name, company, school, email, order):
    p_list = []
    records = order.split(";")
    for r in records:
        parts = r.split(",")
        p_list.append([int(parts[0]), parts[1]])
    price = process_and_email("San Diego", name, company, school, email, p_list);
    return str(price)


app.run(host='0.0.0.0')
