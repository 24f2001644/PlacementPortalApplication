<script setup>

import { ref, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"

import StudentSidebar from "../../components/student/StudentSidebar.vue"
import StudentNavbar from "../../components/student/StudentNavbar.vue"
import StudentPageHeader from "../../components/student/StudentPageHeader.vue"
import StudentSectionCard from "../../components/student/StudentSectionCard.vue"
import StudentLoading from "../../components/student/StudentLoading.vue"

import {

    getDriveDetails,

    applyForDrive

} from "../../services/student"



const route = useRoute()

const router = useRouter()

const driveId = route.params.id

const loading = ref(true)

const applying = ref(false)



const drive = ref({

    drive_id:null,

    company:"",

    role:"",

    description:"",

    package:"",

    location:"",

    eligibility:"",

    deadline:""

})





async function loadDrive(){

    loading.value = true

    try{

        drive.value = await getDriveDetails(

            driveId

        )

    }

    catch(error){

        console.error(error)

        alert("Unable to load drive details")

    }

    finally{

        loading.value = false

    }

}





async function apply(){

    applying.value = true

    try{

        await applyForDrive(

            driveId

        )



        alert("Applied Successfully")



        router.push(

            "/student/applications"

        )

    }

    catch(error){

        console.error(error)

        alert(

            error.response?.data?.message ||

            "Unable to apply"

        )

    }

    finally{

        applying.value = false

    }

}



onMounted(loadDrive)

</script>

<template>

<div class="student-layout">

    <StudentSidebar />

    <div class="student-content">

        <StudentNavbar />

        <div class="container-fluid mt-4">

            <StudentPageHeader

                title="Placement Drive Details"

                subtitle="Review the job details before applying"

            />



            <StudentLoading

                v-if="loading"

            />



            <template v-else>

                <StudentSectionCard

                    title="Drive Information"

                >

                    <div class="row">

                        <div class="col-md-6 mb-4">

                            <table class="table">

                                <tbody>

                                    <tr>

                                        <th>

                                            Company

                                        </th>

                                        <td>

                                            {{ drive.company }}

                                        </td>

                                    </tr>



                                    <tr>

                                        <th>

                                            Job Role

                                        </th>

                                        <td>

                                            {{ drive.role }}

                                        </td>

                                    </tr>



                                    <tr>

                                        <th>

                                            Package

                                        </th>

                                        <td>

                                            {{ drive.package }}

                                        </td>

                                    </tr>



                                    <tr>

                                        <th>

                                            Location

                                        </th>

                                        <td>

                                            {{ drive.location }}

                                        </td>

                                    </tr>



                                    <tr>

                                        <th>

                                            Last Date

                                        </th>

                                        <td>

                                            {{ drive.deadline }}

                                        </td>

                                    </tr>

                                </tbody>

                            </table>

                        </div>





                        <div class="col-md-6">

                            <h5 class="mb-3">

                                Eligibility

                            </h5>

                            <p>

                                {{ drive.eligibility }}

                            </p>



                            <hr>



                            <h5 class="mb-3">

                                Job Description

                            </h5>

                            <p>

                                {{ drive.description }}

                            </p>

                        </div>

                    </div>



                    <div

                        class="d-flex justify-content-end gap-3 mt-4"

                    >

                        <RouterLink

                            to="/student/drives"

                            class="btn btn-outline-secondary"

                        >

                            <i class="bi bi-arrow-left me-2"></i>

                            Back

                        </RouterLink>



                        <button

                            class="btn btn-success"

                            @click="apply"

                            :disabled="applying"

                        >

                            <i class="bi bi-check-circle me-2"></i>

                            {{ applying ? "Applying..." : "Apply Now" }}

                        </button>

                    </div>

                </StudentSectionCard>

            </template>

        </div>

    </div>

</div>

</template>

<style scoped>

.student-layout{

    display:flex;

    min-height:100vh;

    background:#F8FAFC;

}



.student-content{

    flex:1;

}



.container-fluid{

    padding:25px;

}



.table{

    margin-bottom:0;

}



.table th{

    width:35%;

    color:#334155;

    font-weight:600;

    border:none;

    padding:14px 0;

}



.table td{

    color:#0F172A;

    border:none;

    padding:14px 0;

}



h5{

    color:#1E293B;

    font-weight:600;

}



p{

    color:#475569;

    line-height:1.8;

    text-align:justify;

}



hr{

    margin:25px 0;

}



.btn{

    border-radius:12px;

    padding:10px 22px;

    font-weight:600;

}



.btn i{

    font-size:15px;

}



@media(max-width:992px){

    .container-fluid{

        padding:20px;

    }

}



@media(max-width:768px){

    .student-layout{

        flex-direction:column;

    }



    .student-content{

        width:100%;

    }



    .container-fluid{

        padding:15px;

    }



    .d-flex{

        flex-direction:column;

    }



    .btn{

        width:100%;

    }



    .table th,

    .table td{

        display:block;

        width:100%;

        padding:6px 0;

    }

}

</style>