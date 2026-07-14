<script setup>

import { ref, onMounted } from "vue"

import StudentSidebar from "../../components/student/StudentSidebar.vue"
import StudentNavbar from "../../components/student/StudentNavbar.vue"
import StudentPageHeader from "../../components/student/StudentPageHeader.vue"
import StudentSectionCard from "../../components/student/StudentSectionCard.vue"
import StudentLoading from "../../components/student/StudentLoading.vue"

import { getProfile } from "../../services/student"



const loading = ref(true)



const student = ref({

    full_name:"",

    roll_number:"",

    email:"",

    phone:"",

    course:"",

    branch:"",

    cgpa:"",

    graduation_year:"",

    tenth_marks:"",

    twelfth_marks:"",

    skills:"",

    address:"",

    resume_path:""

})



async function loadProfile(){

    try{

        student.value = await getProfile()

    }

    catch(error){

        console.error(error)

        alert("Unable to load profile")

    }

    finally{

        loading.value = false

    }

}



onMounted(loadProfile)

</script>


<template>

<div class="student-layout">

    <StudentSidebar />

    <div class="student-content">

        <StudentNavbar />

        <div class="container-fluid mt-4">

            <StudentPageHeader

                title="My Profile"

                subtitle="View your academic and personal information"

            />



            <StudentLoading

                v-if="loading"

            />



            <template v-else>

                <div class="row g-4">

                    <!-- Personal Information -->

                    <div class="col-lg-6">

                        <StudentSectionCard

                            title="Personal Information"

                        >

                            <table class="table table-borderless mb-0">

                                <tbody>

                                    <tr>

                                        <th width="35%">

                                            Full Name

                                        </th>

                                        <td>

                                            {{ student.full_name }}

                                        </td>

                                    </tr>

                                    <tr>

                                        <th>

                                            Email

                                        </th>

                                        <td>

                                            {{ student.email }}

                                        </td>

                                    </tr>

                                    <tr>

                                        <th>

                                            Phone

                                        </th>

                                        <td>

                                            {{ student.phone }}

                                        </td>

                                    </tr>

                                    <tr>

                                        <th>

                                            Address

                                        </th>

                                        <td>

                                            {{ student.address }}

                                        </td>

                                    </tr>

                                </tbody>

                            </table>

                        </StudentSectionCard>

                    </div>





                    <!-- Academic Information -->

                    <div class="col-lg-6">

                        <StudentSectionCard

                            title="Academic Information"

                        >

                            <table class="table table-borderless mb-0">

                                <tbody>

                                    <tr>

                                        <th width="40%">

                                            Roll Number

                                        </th>

                                        <td>

                                            {{ student.roll_number }}

                                        </td>

                                    </tr>

                                    <tr>

                                        <th>

                                            Course

                                        </th>

                                        <td>

                                            {{ student.course }}

                                        </td>

                                    </tr>

                                    <tr>

                                        <th>

                                            Branch

                                        </th>

                                        <td>

                                            {{ student.branch }}

                                        </td>

                                    </tr>

                                    <tr>

                                        <th>

                                            Graduation Year

                                        </th>

                                        <td>

                                            {{ student.graduation_year }}

                                        </td>

                                    </tr>

                                    <tr>

                                        <th>

                                            CGPA

                                        </th>

                                        <td>

                                            {{ student.cgpa }}

                                        </td>

                                    </tr>

                                    <tr>

                                        <th>

                                            10th Marks

                                        </th>

                                        <td>

                                            {{ student.tenth_marks }}

                                        </td>

                                    </tr>

                                    <tr>

                                        <th>

                                            12th Marks

                                        </th>

                                        <td>

                                            {{ student.twelfth_marks }}

                                        </td>

                                    </tr>

                                </tbody>

                            </table>

                        </StudentSectionCard>

                    </div>

                </div>





                <div class="row g-4 mt-2">

                    <!-- Skills -->

                    <div class="col-lg-8">

                        <StudentSectionCard

                            title="Skills"

                        >

                            <p class="mb-0">

                                {{ student.skills }}

                            </p>

                        </StudentSectionCard>

                    </div>





                    <!-- Resume -->

                    <div class="col-lg-4">

                        <StudentSectionCard

                            title="Resume"

                        >

                            <a

                                v-if="student.resume_path"

                                :href="student.resume_path"

                                target="_blank"

                                class="btn btn-primary w-100"

                            >

                                <i class="bi bi-download me-2"></i>

                                Download Resume

                            </a>



                            <button

                                v-else

                                class="btn btn-secondary w-100"

                                disabled

                            >

                                Resume Not Uploaded

                            </button>



                            <RouterLink

                                to="/student/profile/edit"

                                class="btn btn-outline-primary w-100 mt-3"

                            >

                                <i class="bi bi-pencil-square me-2"></i>

                                Edit Profile

                            </RouterLink>

                        </StudentSectionCard>

                    </div>

                </div>

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

    color:#475569;

    font-weight:600;

    width:40%;

    padding:12px 0;

}



.table td{

    color:#0F172A;

    padding:12px 0;

}



p{

    color:#334155;

    line-height:1.7;

    margin-bottom:0;

}



.btn{

    border-radius:12px;

    padding:12px;

    font-weight:600;

}



.btn i{

    font-size:16px;

}



@media(max-width:992px){

    .container-fluid{

        padding:18px;

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



    .table th,

    .table td{

        display:block;

        width:100%;

        padding:6px 0;

    }

}

</style>