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

    product_table = "{0:10} {1:20} {2:15} {3:15} \n".format("Quatity", "Product", "Unit Price", "Total Price")
    for product in product_list:
        product_table = product_table + "{0:10} {1:20} {2:15} {3:15} \n".format(str(product[0]), product[1], str(pricing_map[product[1]]), str(pricing_map[product[1]] * product[0]))

    email_body = email_body + product_table + "\n"
    email_body = email_body + \
                 "The total amount of your order is $" + str(get_all_product_price(product_list)) + ". Please make your payment within 30 days. Thank you so much for the business. We hope to see you again! \n\n" + \
                 "Audio Glass Sales Department \n" + datetime.date.today().strftime("%B %d, %Y")
    return email_body

def send_email(email, email_body):
    gmail_user = 'yu.sun.eusa@gmail.com'
    gmail_password = 'Justdoit!'

    sent_from = gmail_user
    to = ['lihoward07@gmail.com']
    subject = 'Alloy Cube'
    body = 'Your Sales Order is Here Finally'

    email_text = """\ 
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent!')

    except:
        print('Something went wrong...')

print(generate_email_body("San Diego", "Howard Li", "Audio Glasses Inc.", "Univ HS", "howardli07@gmail.com", product_list))





