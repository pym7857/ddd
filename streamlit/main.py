import streamlit as st
import pandas as pd

df = pd.read_csv('./pool.xlsx')

st.write('''
# 풀빌라 리스트 
''')
print(df)

test = df.astype(str)
st.dataframe(test)

st.markdown('# 사진')

sunset_imgs = [
    './pics/IMG_3448.JPG', 
    './pics/IMG_3449.JPG', 
    './pics/IMG_3450.JPG', 
    './pics/IMG_3451.JPG', 
    './pics/IMG_3452.JPG', 
    './pics/IMG_3454.JPG', 
    './pics/IMG_3455.JPG', 
    './pics/IMG_3456.JPG', 
    './pics/IMG_3457.JPG', 
    './pics/IMG_3458.JPG', 
    './pics/IMG_3459.JPG', 
    './pics/IMG_3460.JPG', 
    './pics/IMG_3461.JPG', 
    './pics/IMG_3462.JPG', 
    './pics/IMG_3463.JPG', 
    './pics/IMG_3464.JPG', 
    './pics/IMG_3465.JPG', 
    './pics/IMG_3466.JPG', 
    './pics/IMG_3467.JPG', 
    './pics/IMG_3468.JPG', 
    './pics/IMG_3469.JPG', 
    './pics/IMG_3470.JPG', 
    './pics/IMG_3471.JPG', 
    './pics/IMG_3472.JPG', 
    './pics/IMG_3473.JPG', 
    './pics/IMG_3474.JPG', 
    './pics/IMG_3475.JPG', 
    './pics/IMG_3476.JPG', 
    './pics/IMG_3477.JPG', 
]
# image_iterator = paginator("사진 갤러리", sunset_imgs)
# indices_on_page, images_on_page = map(list, zip(*image_iterator))
# st.image(images_on_page, width=100, caption=indices_on_page)

# for idx, img in enumerate(sunset_imgs): 
#         cols = st.columns(4) 
#         cols[0].image(sunset_imgs[idx], use_column_width=True)
#         idx+=1
#         cols[1].image(sunset_imgs[idx], use_column_width=True)
#         idx+=idx
#         cols[2].image(sunset_imgs[idx], use_column_width=True)
#         idx+=idx
#         cols[3].image(sunset_imgs[idx], use_column_width=True)
#         idx+=idx

col1, col2, col3 = st.columns(3)

with col1:
    st.header("에스쁘아")
    st.image("./pics/IMG_3464.JPG")
    st.image("./pics/IMG_3465.JPG")

with col2:
    st.header("인갤러리")
    st.image("./pics/IMG_3476.JPG")
    st.image("./pics/IMG_3477.JPG")

with col3:
    st.header("체리블라썸")
    st.image("./pics/IMG_3448.JPG")
    st.image("./pics/IMG_3449.JPG")

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("구룡포2021")
    st.image("./pics/IMG_3451.JPG")
    st.image("./pics/IMG_3452.JPG")

with col2:
    st.header("비치드")
    st.image("./pics/IMG_3450.JPG")

with col3:
    st.header("마린테라스")
    st.image("./pics/IMG_3466.JPG")
    st.image("./pics/IMG_3467.JPG")

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.header("더뷰1151")
    st.image("./pics/IMG_3468.JPG")
    st.image("./pics/IMG_3469.JPG")

with col2:
    st.header("더뷰1151")
    st.image("./pics/IMG_3470.JPG")
    st.image("./pics/IMG_3471.JPG")

with col3:
    st.header("더뷰1151")
    st.image("./pics/IMG_3472.JPG")
    st.image("./pics/IMG_3473.JPG")

with col4:
    st.header("더뷰1151")
    st.image("./pics/IMG_3474.JPG")
    st.image("./pics/IMG_3475.JPG")
