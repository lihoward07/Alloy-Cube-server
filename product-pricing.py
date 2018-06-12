import datetime
import smtplib

pricing_map = {}
pricing_map["audio glass"] = 249.99
pricing_map["audio glasses"] = 249.99
pricing_map["insurance"] = 50
pricing_map["speaker"] = 50
pricing_map["speakers"] = 50
pricing_map["earphone"] = 20
pricing_map["earphones"] = 20
pricing_map["headphone"] = 20
pricing_map["headphones"] = 20
pricing_map["sun glasses"] = 50
pricing_map["sunglasses"] = 50

product_list = []
product_list.append([2, "audio glasses"])
product_list.append([1, "insurance"])
product_list.append([3, "headphones"])

def get_all_product_price(product_list):
    total_price = 0
    for product in product_list:
        total_price = total_price + product[0] * pricing_map[product[1]]
    return total_price

print(get_all_product_price(product_list))

def generate_email_body(place, name, company, school, email, product_list):
    email_body = "Hi " + name + ", " + "\n\n" + \
                 "This is Virtual Enterprise company Audio Glass. " + \
                 "You have made a purchase from our company at the " + place + " trade show. The following is your order: \n\n"

    product_table = "{0:20} | {1:20} | {2:15} | {3:15} \n".format("Quatity", "Product", "Unit Price", "Total Price")
    for product in product_list:
        product_table = product_table + "{0:20} | {1:20} | {2:15} | {3:15} \n".format(str(product[0]), product[1], str(pricing_map[product[1]]), str(pricing_map[product[1]] * product[0]))

    product_table = product_table + "{0:10} {1:20} {2:15} {3:15} \n".format("Tax", "", "", str(get_all_product_price(product_list) * 0.08))
    email_body = email_body + product_table + "\n"
    email_body = email_body + \
                 "The total amount of your order is $" + str(get_all_product_price(product_list) * 1.08) + ". Please make your payment within 30 days. Thank you so much for the business. We hope to see you again! \n\n" + \
                 "Audio Glass Sales Department \n" + datetime.date.today().strftime("%B %d, %Y")
    return email_body

def send_email(email, email_body):
    gmail_user = 'audioglass0@gmail.com'
    gmail_password = 'Aaudioglass0'

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

#hao jijun
process_and_email("San Diego", "Howard Li", "Audio Glasses Inc.", "Univ HS", "lihoward07@gmail.com", product_list)


words = "My first name is howard. My last name is li. My company name is audio glass. My school is university high school. My email is lihoward07@gmail.com." + \
        "I want to order 5 units of audio glasses, 3 units of speakers, and 2 units of headphones."


