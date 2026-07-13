<script setup>

import { ref, onMounted } from "vue"
import { useRoute } from "vue-router"



import CompanySidebar from "../../components/company/CompanySidebar.vue"
import CompanyNavbar from "../../components/company/CompanyNavbar.vue"
import CompanyPageHeader from "../../components/company/CompanyPageHeader.vue"

import CompanySectionCard from "../../components/company/CompanySectionCard.vue"
import CompanyLoading from "../../components/company/CompanyLoading.vue"



import {

    getStudentDetails

} from "../../services/company"





const route = useRoute()



const loading = ref(true)



const student = ref({

    full_name:"",

    roll_number:"",

    graduation_year:"",

    cgpa:"",

    tenth_marks:"",

    twelfth_marks:"",

    course:"",

    branch:"",

    phone:"",

    address:"",

    skills:"",

    resume_path:""

})







async function loadStudent(){



    loading.value=true



    try{



        const response = await getStudentDetails(

            route.params.id

        )



        student.value=response



    }



    catch(error){



        console.error(error)



        alert(

            "Unable to load student details"

        )



    }



    finally{



        loading.value=false



    }


}






onMounted(

    loadStudent

)



</script>


<template>

<div class="company-layout">


    <CompanySidebar />



    <div class="company-content">


        <CompanyNavbar />



        <div class="container-fluid mt-4">



            <CompanyPageHeader

                title="Student Details"

                subtitle="View complete applicant profile"

            />






            <CompanyLoading

                v-if="loading"

            />







            <div v-else class="row g-4">





                <!-- Personal Information -->

                <div class="col-lg-6">



                    <CompanySectionCard

                        title="Personal Information"

                    >



                        <div class="info-item">

                            <label>

                                Name

                            </label>

                            <p>

                                {{ student.full_name }}

                            </p>

                        </div>





                        <div class="info-item">

                            <label>

                                Roll Number

                            </label>

                            <p>

                                {{ student.roll_number }}

                            </p>

                        </div>





                        <div class="info-item">

                            <label>

                                Phone

                            </label>

                            <p>

                                {{ student.phone }}

                            </p>

                        </div>





                        <div class="info-item">

                            <label>

                                Address

                            </label>

                            <p>

                                {{ student.address }}

                            </p>

                        </div>



                    </CompanySectionCard>



                </div>








                <!-- Academic Information -->

                <div class="col-lg-6">



                    <CompanySectionCard

                        title="Academic Information"

                    >



                        <div class="info-item">

                            <label>

                                Course

                            </label>

                            <p>

                                {{ student.course }}

                            </p>

                        </div>





                        <div class="info-item">

                            <label>

                                Branch

                            </label>

                            <p>

                                {{ student.branch }}

                            </p>

                        </div>





                        <div class="info-item">

                            <label>

                                CGPA

                            </label>

                            <p>

                                {{ student.cgpa }}

                            </p>

                        </div>





                        <div class="info-item">

                            <label>

                                Graduation Year

                            </label>

                            <p>

                                {{ student.graduation_year }}

                            </p>

                        </div>



                    </CompanySectionCard>



                </div>









                <!-- Skills & Resume -->

                <div class="col-12">



                    <CompanySectionCard

                        title="Skills & Resume"

                    >



                        <div class="mb-3">


                            <label>

                                Technical Skills

                            </label>



                            <p>

                                {{ student.skills }}

                            </p>



                        </div>







                        <a

                            :href="student.resume_path"

                            target="_blank"

                            class="btn btn-primary"

                        >



                            <i class="bi bi-file-earmark-pdf me-2"></i>


                            View Resume



                        </a>





                    </CompanySectionCard>



                </div>







            </div>





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



.info-item{

    margin-bottom:18px;

}



label{

    display:block;

    font-weight:600;

    color:#475569;

    font-size:14px;

    margin-bottom:6px;

}



p{

    background:#F8FAFC;

    border:1px solid #E2E8F0;

    border-radius:10px;

    padding:12px 15px;

    margin:0;

    color:#0F172A;

    min-height:45px;

    display:flex;

    align-items:center;

}



.btn-primary{

    background:#2563EB;

    border:none;

    border-radius:10px;

    padding:11px 18px;

    font-weight:600;

}



.btn-primary:hover{

    background:#1D4ED8;

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