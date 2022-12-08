import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('model.sav', 'rb'))


def main():
    st.title('Apakah kamu termasuk obesitas?')

    gender = st.selectbox('Jenis Kelamin', ('Laki-laki', 'Perempuan'))
    # aman
    age = st.text_input('Umur')  # aman
    height = st.text_input('Tinggi Badan')  # aman
    weight = st.text_input('Berat Badan')  # aman
    family_history = st.selectbox(
        'Apakah Gemuk Karena Keturunan Keluarga? ', ('Tidak', 'Ya'))  # aman
    consumption_high_caloric_food = st.selectbox(
        'Apakah anda sering makan makanan tinggi kalori? ', ('Tidak', 'Ya'))  # aman
    consumption_vegetables = st.selectbox(
        'Seberapa sering anda makan sayur?', ('Tidak Pernah', 'Kadang-kadang', 'Selalu'))  # aman
    number_main_meals = st.selectbox(
        'Berapa kali anda makan dalam sehari?', ('1', '2', '3', '3+'))  # aman
    consumption_between_meal = st.selectbox(
        'Apakah anda nyemil diantara jam makan?', ('Tidak', 'Sering', 'Kadang-kadang', 'Selalu'))  # aman
    smoke = st.selectbox('Apakah anda merokok?', ('Tidak', 'Ya'))  # aman
    consumption_water_daily = st.selectbox(
        'Seberapa banyak anda mengonsumi air dalam sehari?', ('Kurang dari 1 liter', 'Antara 1 dan 2 L', 'Lebih dari 2 L'))  # aman
    calories_consumption_monitoring = st.selectbox(
        'Apakah anda mengontrol konsumsi kalori?', ('Tidak', 'Ya'))  # aman
    physical_activity_frequency = st.selectbox(
        'Seberapa sering anda berolahraga dalam seminggu', ('Tidak Pernah', '1 atau 2 hari', '2 atau 4 hari', '4 atau 5 hari'))  # aman
    time_using_tech_devices = st.selectbox(
        'Berapa jam anda memakai gadget dalam sehari?', ('0-2 jam', '3-5 jam', 'Lebih dari 5'))
    # aman
    consumption_of_alcohol = st.selectbox(
        'Apakah anda mengonsumsi minuman alkohol?', ('Tidak', 'Sering', 'Kadang-kadang', 'Selalu'))
    # aman
    transportation = st.selectbox(
        'Transportasi apa yang sering anda pakai?', ('Automobile', 'Bike', 'Motorbike', 'Transportasi Publik', 'Jalan Kaki'))
   # aman

    diagnose = ''
    if consumption_vegetables == 'Tidak Pernah':
        consumption_vegetables = 1
    elif consumption_vegetables == 'Kadang-kadang':
        consumption_vegetables = 2
    else:
        consumption_vegetables = 3

    if number_main_meals == '1':
        number_main_meals = 1
    elif number_main_meals == '2':
        number_main_meals = 2
    elif number_main_meals == '3':
        number_main_meals = 3
    else:
        number_main_meals = 4

    if consumption_between_meal == 'Tidak':
        consumption_between_meal = 0
    elif consumption_between_meal == 'Sering':
        consumption_between_meal = 1
    elif consumption_between_meal == 'Kadang-kadang':
        consumption_between_meal = 2
    else:
        consumption_between_meal = 3

    if consumption_water_daily == 'Kurang dari 1 liter':
        consumption_water_daily = 1
    elif consumption_water_daily == 'Antara 1 dan 2 L':
        consumption_water_daily = 2
    else:
        consumption_water_daily = 3

    if physical_activity_frequency == 'Tidak Pernah':
        physical_activity_frequency = 0
    elif physical_activity_frequency == '1 atau 2 hari':
        physical_activity_frequency = 1
    elif physical_activity_frequency == '2 atau 4 hari':
        physical_activity_frequency = 2
    else:
        physical_activity_frequency = 3

    if time_using_tech_devices == '0-2 jam':
        time_using_tech_devices = 0
    elif time_using_tech_devices == '3-5 jam':
        time_using_tech_devices = 1
    else:
        time_using_tech_devices = 2

    if consumption_of_alcohol == 'Tidak':
        consumption_of_alcohol = 0
    elif consumption_of_alcohol == 'Sering':
        consumption_of_alcohol = 1
    elif consumption_of_alcohol == 'Kadang-kadang':
        consumption_of_alcohol = 2
    else:
        consumption_of_alcohol = 3

    if gender == 'Laki-laki':
        gender_male = 1
        gender_female = 0
    else:
        gender_female = 1
        gender_male = 0

    if family_history == 'Tidak':
        family_history_no = 1
        family_history_yes = 0
    else:
        family_history_no = 0
        family_history_yes = 1

    if consumption_high_caloric_food == 'Tidak':
        consumption_high_caloric_food_no = 1
        consumption_high_caloric_food_yes = 0
    else:
        consumption_high_caloric_food_no = 0
        consumption_high_caloric_food_yes = 1

    if smoke == 'Tidak':
        smoke_no = 1
        smoke_yes = 0
    else:
        smoke_no = 0
        smoke_yes = 1

    if calories_consumption_monitoring == 'Tidak':
        calories_consumption_monitoring_no = 1
        calories_consumption_monitoring_yes = 0
    else:
        calories_consumption_monitoring_no = 0
        calories_consumption_monitoring_yes = 1

    if transportation == 'Automobile':
        transportation_automobile = 1
        transportation_bike = 0
        transportation_motorbike = 0
        transportation_public_transportation = 0
        transportation_walking = 0
    elif transportation == 'Bike':
        transportation_automobile = 0
        transportation_bike = 1
        transportation_motorbike = 0
        transportation_public_transportation = 0
        transportation_walking = 0
    elif transportation == 'Motorbike':
        transportation_automobile = 0
        transportation_bike = 0
        transportation_motorbike = 1
        transportation_public_transportation = 0
        transportation_walking = 0
    elif transportation == 'Transportasi Publik':
        transportation_automobile = 0
        transportation_bike = 0
        transportation_motorbike = 0
        transportation_public_transportation = 1
        transportation_walking = 0
    else:
        transportation_automobile = 0
        transportation_bike = 0
        transportation_motorbike = 0
        transportation_public_transportation = 0
        transportation_walking = 1

    if st.button('Lihat Hasil'):
        diagnose = obesity_predict(
            [consumption_between_meal,
             consumption_of_alcohol,
             gender_male,
             gender_female,
             family_history_no,
             family_history_yes, consumption_high_caloric_food_no, consumption_high_caloric_food_yes,
             smoke_no,
             smoke_yes,
             calories_consumption_monitoring_no, calories_consumption_monitoring_yes, transportation_automobile,
             transportation_bike,
             transportation_motorbike, transportation_public_transportation, transportation_walking,
             age, height, weight,
             consumption_vegetables,
             number_main_meals,
             consumption_water_daily, physical_activity_frequency, time_using_tech_devices])

    st.success(diagnose)


def obesity_predict(input_data):
    input_array = np.asarray(input_data)
    re = input_array.reshape(1, -1)
    prediction = loaded_model.predict(re)
    print(prediction)

    if prediction[0] == 0:
        return 'Insufficient Weight'
    elif prediction[0] == 1:
        return 'Normal Weight'
    elif prediction[0] == 2:
        return 'Obesity Type I'
    elif prediction[0] == 3:
        return 'Obesity Type II'
    elif prediction[0] == 4:
        return 'Obesity Type III'
    elif prediction[0] == 5:
        return 'Overweight Level I'
    else:
        return 'Overweight Level II'


if __name__ == '__main__':
    main()
