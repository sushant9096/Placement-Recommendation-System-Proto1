# <==== Importing Dependencies ====>
import re

import streamlit as st
import pandas as pd

# <==== Code starts here ====>

jobs_list = pd.read_hdf('src/models/jobs.hdf5', 'jobs', 'r')
import h5py
with h5py.File('src/models/jobs.hdf5', 'r') as f:
    dset = f['similarity']
    similarity = dset


    def recommend_job(job):
        for ind in jobs_list.index:
            if re.search(job, jobs_list['job_post'][ind], re.IGNORECASE):
                index = ind
                break

        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        job_names = []
        company_names = []
        cos_similarity = []
        posted_on = []
        # print(distances)
        for i in distances[1:21]:
            job_name = jobs_list.iloc[i[0]].job_post
            company = jobs_list.iloc[i[0]]['company']
            posted = jobs_list.iloc[i[0]]['posted_on']
            job_names.append(job_name)
            company_names.append(company)
            cos_similarity.append(i[1])
            posted_on.append(posted)
            # recommended_course_names.append(course(course_name, course_url))

        recommended_courses = pd.DataFrame({
            "Job": job_names,
            "Company": company_names,
            "cos_similarity": cos_similarity,
            "posted_on": posted_on,
        })
        return recommended_courses


    st.markdown(
        f"""
             <style>
             .stApp {{
                 background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
                 background-attachment: fixed;
                 background-size: cover
             }}
             </style>
             """,
        unsafe_allow_html=True
    )
    st.markdown("<h2 style='text-align: center; color: blue;'>Placement Recommendation System</h2>",
                unsafe_allow_html=True)
    st.markdown(
        "<h4 style='text-align: center; color: black;'>Find similar placements from a dataset of over 37,556 jobs from Naukri.com!</h4>",
        unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: black;'>Web App created by  Your Name</h4>",
                unsafe_allow_html=True)

    job_list = jobs_list['job_post'].values
    selected_course = st.text_input("Enter Job Title",)
    # selected_course = st.selectbox(
    #     "Type or select a job you like :",
    #     jobs_list
    # )

    if st.button('Show Recommended Placements'):
        st.write("Recommended Placement based on your interests are :")
        recommended_course_names = recommend_job(selected_course)
        st.table(recommended_course_names)
        # st.text(recommended_course_names[0].name)
        # st.text(recommended_course_names[1])
        # st.text(recommended_course_names[2])
        # st.text(recommended_course_names[3])
        # st.text(recommended_course_names[4])
        # st.text(recommended_course_names[5])
        # st.text(" ")
        st.markdown(
            "<h6 style='text-align: center; color: red;'>Copyright reserved by Coursera and Respective Course Owners</h6>",
            unsafe_allow_html=True)

# <==== Code ends here ====>