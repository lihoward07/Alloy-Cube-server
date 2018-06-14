import datetime
import smtplib
from flask import Flask
app = Flask(__name__)


email_map = {'1':'audioglass0@gmail.com', '2':'yu.sun.eusa@gmail.com'}
email_password_map = {'1':'paulgeorgePG13', '2':'Justdoit!'}

company_map = {}
company_map['1'] = "Audio Glass"
company_map['2'] = "Apple Inc."

pricing_map = {}
pricing_map["Audio Glass"] = 249.99
pricing_map["Audio Glasses"] = 249.99
pricing_map["Insurance"] = 50
pricing_map["Speaker"] = 50
pricing_map["Speakers"] = 50
pricing_map["Headphones"] = 20
pricing_map["Headphone"] = 20
pricing_map["Sunglasses"] = 50

pricing_map2 = {}
pricing_map2["Macbook"] = 789
pricing_map2["iPhone 8"] = 699
pricing_map2["iWatch"] = 499
pricing_map2["Mac Pro"] = 510
pricing_map2["Mac Mini"] = 260


def get_price(company, product):
    toSearch = product
    if "(" in product:
        toSearch = product.split("(")[0]
    if company == '1':
        return pricing_map[toSearch]
    else:
        return pricing_map2[toSearch]

def get_all_product_price(company_app, product_list):
    total_price = 0
    for product in product_list:
        total_price = total_price + product[0] * get_price(company_app, product[1])
    return round(total_price, 2)

def generate_email_body(company_app, name, company, school, email, product_list):
    place = "San Diego"
    email_body = "Hi " + name + ", " + "\n\n" + \
                 "This is Virtual Enterprise company " + company_map[company_app] + "Audio Glass. " + \
                 "You have made a purchase from our company at the " + place + " trade show. The following is your order: \n\n"

    product_table = "{0:20} {1:20} {2:15} {3:15} \n".format("Quatity", "Product", "Unit Price", "Total Price")
    for product in product_list:
        product_table = product_table + "{0:20} {1:20} {2:15} {3:15} \n".format(str(product[0]), product[1], str(get_price(company_app, product[1])), str(get_price(company_app, product[1]) * product[0]))

    product_table = product_table + "{0:10} {1:20} {2:15} {3:15} \n".format("Tax", "", "", str(round(get_all_product_price(company_app, product_list) * 0.08, 2)))
    email_body = email_body + product_table + "\n"
    email_body = email_body + \
                 "The total amount of your order is $" + str(round(get_all_product_price(company_app, product_list) * 1.08, 2)) + ". Please make your payment within 30 days. Thank you so much for the business. We hope to see you again! \n\n" + \
                 company_map[company_app] + " Sales Department \n" + datetime.date.today().strftime("%B %d, %Y")
    return email_body

def send_email(company_app, email, email_body):
    gmail_user = email_map[company_app]
    gmail_password = email_password_map[company_app]

    sent_from = gmail_user
    to = [email]
    subject = company_map[company_app] + ' Sales Order'
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

def process_and_email(company_app, name, company, school, email, product_list):
    email_body = generate_email_body(company_app, name, company, school, email, product_list)
    print(email_body)
    send_email(company_app, email, email_body)
    total_price = get_all_product_price(company_app, product_list) * 1.08
    return round(total_price, 2)

@app.route("/order/<company_app>/<name>/<company>/<school>/<email>/<order>")
def make_order(company_app, name, company, school, email, order):
    p_list = []
    records = order.split(";")
    for r in records:
        parts = r.split(",")
        p_list.append([int(parts[0]), parts[1]])
    price = process_and_email(str(company_app), name, company, school, email, p_list);
    return str(price)


app.run(host='0.0.0.0')
