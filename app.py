import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('model.sav', 'rb'))


def main():
    st.title('Apakah kamu termasuk obesitas?')

    age = st.text_input('Umur')
    height = st.text_input('Tinggi Badan')
    weight = st.text_input('Berat Badan')
    consumption_between_meal = st.text_input(
        'Konsumsi Makanan diantara Makan Pokok (0=Tidak, 1=Sering, 2=Kadang-kadang, 3=Selalu)')
    consumption_of_alcohol = st.text_input(
        'Konsumsi Alkohol (0=Tidak, 1=Sering, 2=Kadang-kadang, 3=Selalu)')
    gender = st.text_input('Jenis Kelamin (0=Male, 1=Female)')
    family_history = st.text_input('Keturunan gemuk (0=No, 1=Yes)')
    consumption_high_caloric_food = st.text_input(
        'Konsumsi Makan Tinggi Kalori (0=No, 1=Yes)')
    smoke = st.text_input('Merokok (0=No, 1=Yes)')
    calories_consumption_monitoring = st.text_input(
        'Cek Konsumsi Kalori Secara Berkala (0=no, 1=yes)')
    transportation = st.text_input(
        'Transportasi Yang Sering Dipakai (0=Automobile, 1=Bike, 2=Motorbike, 3=Transportasi Publik, 4=Jalan Kaki)')
    consumption_vegetables = st.text_input(
        'Konsumsi Sayur (1=Tidak Pernah, 2=Kadang-kadang, 3=Selalu)')
    number_main_meals = st.text_input(
        'Sekali makan dalam sehari (1=1, 2=2, 3=3,4=3+)')
    consumption_water_daily = st.text_input(
        'Konsumsi Air Putih Dalam Sehari (1=Less than a liter , 2=Between 1 and 2 L, 3=More than 2 L )')
    physical_activity_frequency = st.text_input(
        'Olahraga dalam seminggu (0=I do not have , 1=1 or 2 days, 2=2 or 4 days , 3=4 or 5 days )')
    time_using_tech_devices = st.text_input(
        'Pemakaian Gadget (0=0-2 hours, 1=3-5 hours, 2=More than 5 hours )')

    diagnose = ''

    if gender == 0:
        gender_male = 1
        gender_female = 0
    else:
        gender_female = 0
        gender_male = 1

    if family_history == 0:
        family_history_no = 1
        family_history_yes = 0
    else:
        family_history_no = 0
        family_history_yes = 1

    if consumption_high_caloric_food == 0:
        consumption_high_caloric_food_no = 1
        consumption_high_caloric_food_yes = 0
    else:
        consumption_high_caloric_food_no = 0
        consumption_high_caloric_food_yes = 1

    if smoke == 0:
        smoke_no = 1
        smoke_yes = 0
    else:
        smoke_no = 0
        smoke_yes = 1

    if calories_consumption_monitoring == 0:
        calories_consumption_monitoring_no = 1
        calories_consumption_monitoring_yes = 0
    else:
        calories_consumption_monitoring_no = 0
        calories_consumption_monitoring_yes = 1

    if transportation == 0:
        transportation_automobile = 1
        transportation_bike = 0
        transportation_motorbike = 0
        transportation_public_transportation = 0
        transportation_walking = 0
    elif transportation == 1:
        transportation_automobile = 0
        transportation_bike = 1
        transportation_motorbike = 0
        transportation_public_transportation = 0
        transportation_walking = 0
    elif transportation == 2:
        transportation_automobile = 0
        transportation_bike = 0
        transportation_motorbike = 1
        transportation_public_transportation = 0
        transportation_walking = 0
    elif transportation == 3:
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
            [age, height, weight,
             consumption_between_meal,
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
