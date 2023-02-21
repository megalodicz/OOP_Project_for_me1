import time
import streamlit as st
from sklearn import *
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import Page1
import streamlit as st
import Page2

st.set_page_config(
    page_title="Predict Your Car",
    layout="wide",
)
with st.sidebar:
        ot = st.selectbox("Others:",
                      ('Home','Car Type','Motorcycle Type'))

if ot == 'Home':
    st.header("Predict Your Car")

    tab1, tab2, tab3 = st.tabs(["Home", "Car", "Motorcycle"])

    with tab1:
        st.header("Home Page")
        st.info('This Web Made By Jarkapat 65114540084,Made for FinalProject OOP Subject Semester2/2023  ,This Web Use Machinelearning form Libary Scikit-learn'
                'For Users is want to buy some new car but do not know what type car is convenient for them, That is why    I made this web for that users')
        st.caption('Click Button Below this Before Prediction')
        cols = st.columns(2)
        with cols[0]:
            loadb = st.button('1.Load cars.csv')
        if loadb:
            def load_data():
                return pd.DataFrame(
                    {
                        "Hores Power": [120, 200, 180, 200, 250, 250, 300, 500, 800, 800],
                        "Seat": [4, 4, 6, 7, 2, 4, 2, 2, 4, 2],
                        "Option": ['Family', 'Family', 'Trunk', 'Trunk', 'Sport Car', 'Sport Car', 'Sport Car',
                                   'Sport Car', 'Sport Car', 'Sport Car'],
                        "Car": ["ซีดาน (Sedan)", "ซีดาน (Sedan)", "รถพีพีวี (PPV)", "รถพีพีวี (PPV)",
                                'รถเปิดประทุน (Cabrio)',
                                'รถเปิดประทุน (Cabrio)', 'รถเปิดประทุน (Cabrio)', 'รถเปิดประทุน (Cabrio)',
                                'รถเปิดประทุน (Cabrio)', 'รถเปิดประทุน (Cabrio)']
                    }
                )


            df = load_data()
            st.dataframe(df, use_container_width=True)
            st.caption('ตารางโชว์การทำนายรถยนต์')


            def load_motor():
                return pd.DataFrame(
                    {
                        " fetures": [50, 100, 125, 150, 150, 250, 300, 500, 800, 1000],
                        "Option": ['Auto', 'Clutch', 'Auto', 'Auto', 'Clutch', 'Auto', 'Auto', 'Clutch', 'Clutch',
                                   'Clutch', ],
                        "lable": ['Electric Bike', 'Wave', 'Fino', 'Fino', 'Wave', 'XMAX', 'XMAX', 'Big Bike',
                                  'Big Bike', 'Big Bike', ]

                    }
                )


            df = load_motor()
            st.dataframe(df, use_container_width=True)
            st.caption('ตารางโชว์การทำนายรถมอเตอร์ไซค์')
        with cols[1]:
            trainb = st.button('2.Train')
        if trainb:
            with st.spinner('Wait ...'):
                time.sleep(2)
                st.write('training model ...')
            st.success('Sucess!')


    def load_house_data():
        return pd.read_csv('cars.csv')


    def load_model():
        return joblib.load('cars.csv')


    def save_model(model):
        joblib.dump(model, 'cars.csv')


    with tab2:
        st.header("🚗 Car")
        cars = pd.read_csv('cars.csv')
        X = cars[['Horsepower', 'Seats']]
        y = cars['CarType']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        clf = DecisionTreeClassifier()
        clf.fit(X_train, y_train)

        cols = st.columns(2)
        with cols[0]:
            number = st.number_input('Start Horse Power', min_value=1,max_value=1500)
        with cols[1]:
            number1 = st.number_input('How many seat', min_value=1,max_value=8)

        x = (number, number1)
        pred1 = np.asarray(x)
        pred2 = pred1.reshape(1, -1)

        op = []
        option = st.selectbox(
            'More option?',
            ('Family', 'Trunk', 'Sport Car'))
        op.append(option)
        st.caption('Ex : Horse Power < 250 = Family : Car Seat > 4 = Trunk : Horse Power > 500 = Sport Car : Car Seat < 4')

        realpre = clf.predict(pred2)
        if st.button('Submit'):
            if realpre == ['Cabrio'] and op == ['Sport Car']:
                with st.spinner('Wait ...'):
                    time.sleep(2)
                    st.subheader('รถเปิดประทุน (Cabrio) หรือ สปอร์ตคาร์ (Sportcar)')
                    image2 = Image.open('sportcar.jpg')
                    st.image(image2, caption='Sport Car')
                    st.markdown(
                        'รถยนต์ Sport Car เป็นรถยนต์ที่สามารถขับขี่ได้จริงในชีวิตประจำวันมากกว่า Super Car ส่วนมากจะเน้นเรื่องสมรรถนะไปในด้านการขับขี่ง่าย คล่องตัว กระฉับกระเฉงเวลาขับขี่บนท้องถนน '
                        ' Sport Car ถูกจำแนกไปหลายกลุ่มด้วยกัน เช่น Sport Sedan และ Coupe เป็นต้น '
                        'รถยนต์ประเภทนี้มันจะมีการออกแบบรูปโฉมภายนอกที่สวยงาม ทันสมัย โดดเด่นกว่ารถยนต์ธรรมดาทั่ว ๆ ไป '
                        'เห็นโดดเด่นมาแต่ไกลว่าคือ Sport Car อีกทั้งภายในจะมีเอกลักษณ์ที่โดดเด่นไปตามแต่ละค่าย '
                        'เช่น Porsche 718 มาพร้อมที่นั่ง 2 ที่ ภายในจะมีความหรูหรา ตามแบบฉบับของ Porsche แต่เพิ่มลูกเล่นเข้ามาให้ดูสปอร์ต เร้าใจมากขึ้น เป็นต้น '
                        'นอกจากนี้รถยนต์ Sport Car จะมีราคาและค่าบำรุงรักษาที่ไม่สูงเท่า Super Car เรื่องขุมพลังและอัตราการเร่งก็ไม่สูงเท่า Super Car เช่นกัน แต่ถือว่าสามารถเอาใจสาย '
                        'Sport ในงบที่เอื้อมถึงได้แบบลงตัวเลยทีเดียว')
                    st.markdown('http://www.brg.co.th')
            elif realpre == ['PPV'] and op == ['Trunk']:
                with st.spinner('Wait ...'):
                    time.sleep(2)
                    st.subheader('รถพีพีวี (PPV) หรือ รถตู้ (Van)')
                    image1 = Image.open('spvcar.jpg')
                    st.image(image1, caption='Family Car')
                    st.markdown('PPV หรือ “รถกระบะดัดแปลงเป็นรถยนต์นั่งอเนกประสงค์” '
                                'คือ รถยนต์ที่มีการดัดแปลงมาจากรถกระบะ หรือเป็นรถยนต์ที่ใช้ตัวถัง (Chassis) แบบเดียวกับรถกระบะ แต่จะมีการปรับแต่งช่วงล่างเพื่อเพิ่มความนิ่มนวลในการขับขี่ รถยนต์ PPV นี้ ถือเป็นประเภทรถยนต์ที่มีเฉพาะในประเทศไทยเท่านั้น '
                                'เนื่องจากเป็นคำนิยามที่กรมสรรพสามิตใช้เรียกเพื่อกำหนดมูลค่าภาษี แต่บางครั้งก็มักจะถูกเรียกรวมอยู่ในประเภทของรถยนต์ SUV เช่นกัน'
                                'ตัวอย่างของรถยนต์ PPV อาทิ Isuzu Mu-X (พื้นฐานเดิมจาก Isuzu D-Max), Toyota Fortuner (พื้นฐานเดิมจาก Toyota REVO) และ Mitsubishi Pajero Sport (พื้นฐานเดิมจาก Mitsubishi Triton) ฯลฯ'
                                'จุดเด่นของรถยนต์ PPV'
                                'เป็นรถยนต์สมรรถนะสูง รองรับการขับขี่ที่สมบุกสมบันได้สบาย เนื่องจากมีพื้นฐานของรถกระบะ'
                                'สามารถบรรทุกสัมภาระขนาดใหญ่ได้ ไม่ต่างจากรถกระบะทั่วไป'
                                'มักมีการปรับช่วงล่างจากระบบแหนบของรถกระบะ ให้เป็นระบบคอยล์สปริง ส่งผลให้การขับขี่และการโดยสารมีความนุ่มนวลมากกว่ารถกระบะ')
                    st.markdown('https://www.easysunday.com')
            elif realpre == ['Sedan'] and op == ['Family']:
                with st.spinner('Wait ...'):
                    time.sleep(2)
                    st.subheader("ซีดาน (Sedan) แฮคชืแบ็ก (hatchback) หรือ คูเป้ (coupe)")
                    image = Image.open('secancar.jpg')
                    st.image(image, caption='Sedan Car')
                    st.markdown('สำหรับรถยนต์ประเภท Sedan (ซีดาน) หรือที่บางคนก็เรียกว่ารถยนต์ประเภท Saloon (ซาลูน) '
                                'คือ กลุ่มรถยนต์นั่งส่วนบุคคล หรือรถเก๋งที่มี 4 ประตู ถือว่าเป็นรูปแบบพื้นฐานรูปแบบแรกๆ ของการผลิตรถยนต์ '
                                'ที่มีลักษณะโดยหลักการว่ารถยนต์ประเภท Sedan จะมีการวางเครื่องยนต์อยู่ด้านหน้าของตัวรถ หลังรถมีกระโปรงเก็บของ'
                                ' มีที่นั่งสำหรับผู้โดยสาร 4 ที่นั่งหรือมากกว่า หลังคารถเป็นส่วนหนึ่งของตัวรถ ไม่สามารถถอดออกหรือเปิดประทุนได้ '
                                'ซึ่งไม่ว่าจะเป็นแบบ 4 ประตูหรือ 2 ประตูก็จะเรียกว่ารถยนต์ประเภท Sedan ทั้งหมด แต่ในระยะหลังมักเรียกรถ '
                                'Sedan 2 ประตูว่า Coupe (คูเป้)')
                    st.markdown('https://chobrod.com')

            else:
                st.subheader('ข้อมูลไม่ตรงกับรถรุ่นใดบนโลก')

    with tab3:
        st.header("🏍️ Motorcycle")
        fetures = [[50], [100], [125], [150], [200], [250], [300], [500], [800], [1000]]
        lable = ['Electric Bike', 'Wave', 'Wave', 'Wave', 'XMAX', 'XMAX', 'XMAX', 'Big Bike', 'Big Bike', 'Big Bike', ]
        classifier = tree.DecisionTreeClassifier()
        classifier = classifier.fit(fetures, lable)

        cols = st.columns(2)
        with cols[0]:
            number = st.number_input('Start CC Power', min_value=50,max_value=1000)
        opt = []
        with cols[1]:
            optiont = st.selectbox(
                'More option?',
                ('Clutch', 'Auto'))
            opt.append(optiont)
    

        pre = classifier.predict([[number]])
        if st.button('Enter'):
            if pre == ['Electric Bike'] and opt == ['Auto']:
                with st.spinner('Wait ...'):
                    time.sleep(2)
                    st.subheader('จักรยานไฟฟ้า Electric Bike')
                    image2 = Image.open('eBike.jpg')
                    st.image(image2, caption='Electric Bike')
                    st.markdown(
                        'ปั่นจักรยานแบบประหยัดแรงด้วยจักรยานไฟฟ้าจักรยานไฟฟ้า '
                        'นวัตกรรมที่คิดค้นมาเพื่อเพิ่มความสะดวกสบายในการเดินทาง และกลายเป็นอีกตัวเลือกสำหรับผู้ที่ไม่มีรถยนต์และรถจักรยานยนต์ '
                        'โดยจักรยานไฟฟ้าใช้งานง่าย ขับเคลื่อนด้วยมอเตอร์ และประหยัดแรงกว่าจักรยานทั่วไป จึงเป็นอีกสินค้าที่กำลังได้รับความนิยมในปัจจุบันส่วนประกอบของจักรยานไฟฟ้าจักรยานไฟฟ้า (E-Bike) '
                        'เป็นรูปแบบของยานพาหนะชนิดหนึ่ง มีลักษณะคล้ายรถจักรยานและรถจักรยานยนต์ แต่สามารถประหยัดแรงปั่นได้มากกว่าจักรยานทั่วไป แถมวิธีใช้งานง่ายกว่ารถจักรยานยนต์ ทำให้ E-Bike '
                        'เข้ามามีบทบาทในท้องตลาดแทนที่รถจักรยานและจักรยานยนต์ได้ในเวลาอันรวดเร็ว โดยส่วนประกอบที่ทำให้จักรยานสามารถขับเคลื่อนได้ คือ “มอเตอร์” ซึ่งเป็นจุดแข็งที่ทำให้จักรยานไฟฟ้าประสบความสำเร็จ ')
                    st.markdown('https://www.ktc.co.th')
            elif pre == ['Wave'] and opt == ['Clutch']:
                with st.spinner('Wait ...'):
                    time.sleep(2)
                    st.subheader('รถเวฟ Wave')
                    image1 = Image.open('Wave.jpg')
                    st.image(image1, caption='Wave')
                    st.markdown(
                        'เป็นเวลากว่า 30 ปีที่รถมอเตอร์ไซค์ฮอนด้าอยู่คู่ครอบครัวไทย คอยร่วมฝ่าฟันไปกับผู้ใช้งานในหลาย ๆ จังหวะชีวิต ทั้งเรื่องทุกข์ เรื่องสุข และในทุก ๆ การเดินทาง หลายคนมีประสบการณ์ร่วมกับรถมอเตอร์ไซค์ฮอนด้าในหลากหลายรุ่น '
                        'แตกต่างกันไปตามช่วงเวลา และความชื่นชอบ แต่หากจะนึกถึงหนึ่งตัวแทนแห่งความสัมพันธ์อันยาวนาน ระหว่างรถมอเตอร์ไซค์ฮอนด้ากับคนไทย หลายคนคงจะนึกถึงรถมอเตอร์ไซค์ฮอนด้า ตระกูล “Wave”เชื่อว่าคนไทยส่วนมากคุ้นเคยกับคำว่า'
                        ' “Honda Wave” เป็นอย่างดี ถึงแม้จะไม่เคยมีโอกาสได้ใช้งานก็ตาม เนื่องจาก Honda Wave รุ่นแรกถือกำเนิดขึ้นในประเทศไทยตั้งแต่ปี พ.ศ. 2540 ซึ่งถ้าหากรวมระยะเวลาตั้งแต่วันแรกจนถึงปัจจุบัน ก็เป็นเวลากว่า 20 ปีแล้ว '
                        'ด้วยพื้นฐานของการเป็นรถมอเตอร์ไซค์ประเภทครอบครัว ที่ขับขี่ง่ายและเหมาะกับทุกเพศทุกวัย อีกทั้งยังเป็นรถมอเตอร์ไซค์ที่ขึ้นชื่อว่าประหยัดน้ำมันสุด ๆ ทำให้ Honda Wave ได้มีโอกาสเข้าไปเป็นส่วนหนึ่งในหลาย ๆ ครัวเรือนในประเทศไทย '
                        'และทำให้ Honda Wave ครองตำแหน่งแชมป์ยอดขายมอเตอร์ไซค์ตั้งแต่ปี พ.ศ. 2540 – 2561 สูงสุดอันดับหนึ่งในประเทศไทย ถึง 14.5 ล้านคัน')
                    st.markdown('https://www.thaihonda.co.th')
            elif pre == ['Wave'] and opt == ['Auto']:
                with st.spinner('Wait ...'):
                    time.sleep(2)
                    st.subheader('รถฟีโน่ Fino')
                    image1 = Image.open('Fino.jpg')
                    st.image(image1, caption='Wave')
                    st.markdown(
                        'Yamaha Fino’ (ยามาฮ่า ฟีโน่) เป็นรถมอเตอร์ไซค์ออโตเมติกที่วางจำหน่ายในไทยเมื่อปี ค.ศ. 2006 ซึ่งถือว่าเป็นหนึ่งในรถออโตเมติกรุ่นบุกเบิกของทางบริษัทยามาฮ่า '
                        'ซึ่งในช่วงปีนั้นทางบริษัทจะมีรถออโตเมติกทำตลาดอยู่ 3 รุ่น ได้แก่ Yamaha Nouvo, Yamaha Mio และมี Yamaha Fino เป็นน้องคนสุดท้องจาก 3 รายชื่อรถออโตเมติกที่ถูกกล่าวมานั้น '
                        'เบอร์ 1 เรื่องความฮิตแบบปังๆ ได้ตกเป็นของ Yamaha Mio ด้วยรูปทรงที่ถูกใจวัยรุ่น พร้อมกับบริษัทได้เลือกให้วง Clash เป็นพรีเซนเตอร์ ประจวบเหมาะกับจังหวะที่วงกำลังประสบความสำเร็จในอัลบั้มที่สอง '
                        'พร้อมกับ ‘แบงค์’ นักร้องนำของวงที่ช่วงนั้นไว้ผมทรงโมฮอว์กสุดเท่ องค์ประกอบเหล่านี้ได้ทำให้ Yamaha Mio กลายเป็นรถออโตเมติกที่ฮิตสุดๆ ')
                    st.markdown('https://exoticquixotic.com')
            elif pre == ['XMAX'] and opt == ['Auto']:
                with st.spinner('Wait ...'):
                    time.sleep(2)
                    st.subheader('รถเอ็กซ์แม๊ก XMAX')
                    image1 = Image.open('XMAX.jpg')
                    st.image(image1, caption='XMAX')
                    st.markdown(
                        'Yamaha X-MAX 300 เป็นรถแนว สปอร์ตออโตเมติก ระดับพรีเมี่ยม ของค่าย Yamaha ในตระกูล MAX Series มีเทคโนโลยี BLUE CORE โดดเด่นด้วยไฟหน้า-ไฟท้าย ออกแบบมาได้อย่างสปอร์ต '
                        'ใช้ไฟเป็นแบบ FULL LED ยังมีความทันสมัยอย่าง Smart Key system ระบบกุญแจสมาร์ทคีย์ อัจฉริยะ สตาร์ทรถโดยไม่ต้องใช้กุณแจ และยังมี ANSWER BACK ให้มาอีกด้วย เอ็กซ์แม็กซ์300 ยังมีระบบเบรกแบบ '
                        'ABS ช่วยป้องกันล้อล็อค ระบบ Traction Control System (TCS) ปรับสมดุลเครื่องยนต์ เอ็กซ์แม็กซ์300 มีสีให้เลือก 4 สี คือ สีขาว-ดำ, สีเทา-ดำ, สีน้ำตาล-ดำ-เทา และสีเหลือง-ดำ')
                    st.markdown('https://www.bigbikeinfo.com')
            elif pre == ['XMAX'] and opt == ['Clutch']:
                with st.spinner('Wait ...'):
                    time.sleep(2)
                    st.subheader('รถบิ๊กไบค์ Bigbike')
                    image1 = Image.open('BigBike.jpg')
                    st.image(image1, caption='Bigbike')
                    st.markdown(
                        'Bigbike นั้นมีแหล่งกำเนิดมาจากต่างประเทศ ทั้งอเมริกาและจีน รวมถึงประเทศที่อยู่ในโซนยูโรปอื่นๆ และได้แผร่ขยายมายังโซนเอเชียจนมาถึงบ้านเรา '
                        'แต่ในการเรียกจักรยานยนต์ในบ้านเรานั้นยังคลุมเคลือ ซึ่งตามหลักการสากล รถจักรยานยนต์ที่จะเรียกว่าบิ๊กไบค์นั้น จะต้องมีเครื่องยนต์ขนาดตั้งแต่ 250cc ขึ่นไป ดังนั้นถ้ายึดหลักการตามหลักสากล '
                        'บิ๊กไบค์ คือรถจักรยานยนต์ที่มีขนาดเครื่องยนต์ ตั้งแต่ 250cc ขึ้นไปก็จะถือว่าเป็นบิ๊กไบค์จักรยานยนต์ที่ถูกเรียกว่าบิ๊กไบค์คันแรกของคาวาซากิ คือรุ่น Kawasaki W1 ซึ่งเกิดขึ่นตั้งแต่ปี 1965และจักรยานยนต์บิ๊กไบค์ที่นำเข้ามาในประเทศไทย(รถใหม่มือหนึ่ง) '
                        'ค่ายแรกก็คือ Kawasaki เป็นรุ่น Ninja250แต่พอเอาเข้าจริง นิยามของคำว่า บิ๊กไบค์ นั้นอยู่ที่ตัวคุณ หากคุณคิดว่านั่นคือบิ๊กไบค์ ไม่ว่าจะเป็นรถ 250 cc. หรือ 1000 cc. นั่นแหล่ะคือบิ๊กไบค์ ไม่จำเป็นต้องสนใจนิยามบิ๊กไบค์ของคนอื่น '
                        'หากมีใครถามหรือสงสัยว่า รถที่ขี่ใช่รถบิ๊กไบค์ไหม ตอบเค้าดังๆเลยว่า "นี่แหล่ะ บิ๊กไบค์ของผม"')
                    st.markdown('https://blogs.peeramotosports.co.th')
            elif pre == ['Big Bike'] and opt == ['Clutch']:
                with st.spinner('Wait ...'):
                    time.sleep(2)
                    st.subheader("รถบิ๊กไบค์ Bigbike")
                    image = Image.open('BigBike.jpg')
                    st.image(image, caption='Bigbike')
                    st.markdown(
                        'Bigbike นั้นมีแหล่งกำเนิดมาจากต่างประเทศ ทั้งอเมริกาและจีน รวมถึงประเทศที่อยู่ในโซนยูโรปอื่นๆ '
                        'และได้แผร่ขยายมายังโซนเอเชียจนมาถึงบ้านเรา แต่ในการเรียกจักรยานยนต์ในบ้านเรานั้นยังคลุมเคลือ ซึ่งตามหลักการสากล รถจักรยานยนต์ที่จะเรียกว่าบิ๊กไบค์นั้น '
                        'จะต้องมีเครื่องยนต์ขนาดตั้งแต่ 250cc ขึ่นไป ดังนั้นถ้ายึดหลักการตามหลักสากล บิ๊กไบค์ คือรถจักรยานยนต์ที่มีขนาดเครื่องยนต์ ตั้งแต่ 250cc ขึ้นไปก็จะถือว่าเป็นบิ๊กไบค์จักรยานยนต์ที่ถูกเรียกว่าบิ๊กไบค์คันแรกของคาวาซากิ '
                        'คือรุ่น Kawasaki W1 ซึ่งเกิดขึ่นตั้งแต่ปี 1965และจักรยานยนต์บิ๊กไบค์ที่นำเข้ามาในประเทศไทย(รถใหม่มือหนึ่ง) ค่ายแรกก็คือ Kawasaki เป็นรุ่น Ninja250แต่พอเอาเข้าจริง นิยามของคำว่า บิ๊กไบค์ นั้นอยู่ที่ตัวคุณ '
                        'หากคุณคิดว่านั่นคือบิ๊กไบค์ ไม่ว่าจะเป็นรถ 250 cc. หรือ 1000 cc. นั่นแหล่ะคือบิ๊กไบค์ ไม่จำเป็นต้องสนใจนิยามบิ๊กไบค์ของคนอื่น หากมีใครถามหรือสงสัยว่า รถที่ขี่ใช่รถบิ๊กไบค์ไหม ตอบเค้าดังๆเลยว่า "นี่แหล่ะ บิ๊กไบค์ของผม"')
                    st.markdown('https://blogs.peeramotosports.co.th')
            else:
                st.subheader('ข้อมูลไม่ตรงกับรถรุ่นใดบนโลก')



if  ot == 'Car Type' :
        Page1.page1()

if ot == 'Motorcycle Type':
        Page2.page2()
