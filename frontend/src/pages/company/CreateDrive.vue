<script setup>

import { ref } from "vue"
import { useRouter } from "vue-router"


import CompanySidebar from "../../components/company/CompanySidebar.vue"
import CompanyNavbar from "../../components/company/CompanyNavbar.vue"
import CompanyPageHeader from "../../components/company/CompanyPageHeader.vue"
import CompanySectionCard from "../../components/company/CompanySectionCard.vue"


import {
    createDrive
} from "../../services/company"



const router = useRouter()



const loading = ref(false)

const branches = [

    "CSE",

    "IT",

    "AIML",

    "CSDS",

    "ECE",

    "EEE",

    "ME",

    "CE"

]

const drive = ref({

    job_title: "",

    job_description: "",

    salary_package: "",

    interview_location: "",

    eligible_branches: "",

    eligible_cgpa: "",

    eligible_year: "",

    application_deadline: "",

    interview_date: ""

})





async function submitDrive(){


    loading.value = true



    try{


        await createDrive(

            drive.value

        )



        alert(

            "Placement drive created successfully"

        )



        router.push(

            "/company/drives"

        )


    }


    catch(error){


        console.error(error)



        alert(

            "Unable to create drive"

        )


    }


    finally{


        loading.value=false


    }


}



</script>
<template>

<div class="company-layout">


    <CompanySidebar />


    <div class="company-content">


        <CompanyNavbar />



        <div class="container-fluid mt-4">



            <CompanyPageHeader

                title="Create Placement Drive"

                subtitle="Create a new hiring opportunity for students"

            />





            <CompanySectionCard

                title="Drive Details"

            >



                <form

                    @submit.prevent="submitDrive"

                >



                    <div class="row g-4">





                        <!-- Role -->

                        <div class="col-md-6">


                            <label>

                                Job Role

                            </label>


                            <input

                                type="text"

                                class="form-control"

                                placeholder="Software Engineer"

                                v-model="drive.job_title"

                                required

                            >


                        </div>





                        <!-- Package -->

                        <div class="col-md-6">


                            <label>

                                Package

                            </label>


                            <input

                                type="text"

                                class="form-control"

                                placeholder="12 LPA"

                                v-model="drive.salary_package"

                                required

                            >


                        </div>






                        <!-- Location -->

                        <div class="col-md-6">


                            <label>

                                Location

                            </label>


                            <input

                                type="text"

                                class="form-control"

                                placeholder="Bangalore"

                                v-model="drive.interview_location"

                                required

                            >


                        </div>






                        <!-- Deadline -->

                        <div class="col-md-6">


                            <label>

                                Application Deadline

                            </label>


                            <input

                                type="date"

                                class="form-control"

                                v-model="drive.application_deadline"

                                required

                            >


                        </div>







                        <!-- Eligibility -->

                        <div class="col-md-6">


                            <label>

                                Eligibility Criteria

                            </label>


                            <select
    class="form-control"
    v-model="drive.eligible_branches"
    required
>

    <option value="">
        Select Eligible Branch
    </option>

    <option
        v-for="branch in branches"
        :key="branch"
        :value="branch"
    >
        {{ branch }}
    </option>

</select>


                        </div>






                        <!-- Description -->

                        <div class="col-12">


                            <label>

                                Job Description

                            </label>



                            <textarea

                                rows="5"

                                class="form-control"

                                placeholder="Describe role responsibilities..."

                                v-model="drive.job_description"

                                required

                            ></textarea>


                        </div>


                        <div class="col-md-6">
                            <label>Minimum CGPA</label>

                            <input
                                type="number"
                                step="0.01"
                                class="form-control"
                                v-model="drive.eligible_cgpa"
                                placeholder="7.5"
                                required
                            >
                        </div>

                        <div class="col-md-6">
                            <label>Eligible Year</label>

                            <select
                                class="form-control"
                                v-model="drive.eligible_year"
                                required
                            >
                                <option value="">Select Year</option>
                                <option value="2">2nd Year</option>
                                <option value="3">3rd Year</option>
                                <option value="4">4th Year</option>
                            </select>
                        </div>


                        <div class="col-md-6">
                            <label>Interview Date</label>

                            <input
                                type="date"
                                class="form-control"
                                v-model="drive.interview_date"
                            >
                        </div>





                    </div>






                    <div class="mt-4">


                        <button

                            type="submit"

                            class="btn btn-success w-100"

                            :disabled="loading"

                        >



                            <span v-if="loading">

                                Creating Drive...

                            </span>



                            <span v-else>


                                <i class="bi bi-plus-circle me-2"></i>


                                Create Drive


                            </span>



                        </button>


                    </div>





                </form>



            </CompanySectionCard>



        </div>



    </div>



</div>



</template>

<style scoped>

.company-layout{

    display:flex;

    min-height:100vh;

    background:#F8FAFC;

}



.company-content{

    flex:1;

    display:flex;

    flex-direction:column;

}



.container-fluid{

    padding:28px;

}



label{

    font-weight:600;

    color:#334155;

    margin-bottom:8px;

    display:block;

}



.form-control{

    padding:12px 15px;

    border-radius:12px;

    border:1px solid #CBD5E1;

    transition:.25s;

}



.form-control:focus{

    border-color:#16A34A;

    box-shadow:0 0 0 .2rem rgba(22,163,74,.15);

}



textarea{

    resize:none;

}



.btn-success{

    background:#16A34A;

    border:none;

    padding:13px;

    border-radius:12px;

    font-weight:600;

}



.btn-success:hover{

    background:#15803D;

}



.btn-success:disabled{

    opacity:.7;

    cursor:not-allowed;

}



@media(max-width:992px){

    .company-layout{

        flex-direction:column;

    }

}



@media(max-width:768px){

    .container-fluid{

        padding:18px;

    }

}

</style>