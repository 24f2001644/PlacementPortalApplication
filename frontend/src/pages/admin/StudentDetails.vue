<script setup>

import { reactive, onMounted, ref } from "vue"
import { useRoute } from "vue-router"

import AdminSidebar from "../../components/admin/AdminSidebar.vue"
import AdminNavbar from "../../components/admin/AdminNavbar.vue"
import AdminPageHeader from "../../components/admin/AdminPageHeader.vue"
import AdminSectionCard from "../../components/admin/AdminSectionCard.vue"
import AdminLoading from "../../components/admin/AdminLoading.vue"

import {
    getStudentDetails
} from "../../services/admin"


const route = useRoute()


const loading = ref(true)



const student = reactive({

    user_id: "",

    full_name: "",

    roll_number: "",

    email: "",

    phone: "",

    course: "",

    branch: "",

    cgpa: "",

    tenth_marks: "",

    twelfth_marks: "",

    skills: "",

    graduation_year: "",

    resume_path: "",
    resume_url:"",

    profile_completed: false

})



async function loadStudent(){


    try{


        const data = await getStudentDetails(

            route.params.id

        )


        Object.assign(student,data)


    }


    catch(error){


        console.error(error)

        alert("Unable to load student details")


    }


    finally{


        loading.value=false


    }


}



onMounted(loadStudent)


</script>




<template>


<div class="admin-layout">


    <AdminSidebar />



    <div class="admin-content">


        <AdminNavbar />



        <div class="container-fluid mt-4">



            <AdminPageHeader

                title="Student Details"

                subtitle="View complete student profile information"

            />




            <AdminLoading

                v-if="loading"

            />




            <AdminSectionCard

                v-else

                title="Student Profile"

            >



            <div class="row">



                <div class="col-md-6">


                    <p>

                        <strong>Name:</strong>

                        {{ student.full_name }}

                    </p>


                    <p>

                        <strong>Roll Number:</strong>

                        {{ student.roll_number }}

                    </p>


                    <p>

                        <strong>Email:</strong>

                        {{ student.email }}

                    </p>


                    <p>

                        <strong>Phone:</strong>

                        {{ student.phone }}

                    </p>


                    <p>

                        <strong>Course:</strong>

                        {{ student.course }}

                    </p>


                    <p>

                        <strong>Branch:</strong>

                        {{ student.branch }}

                    </p>


                </div>




                <div class="col-md-6">


                    <p>

                        <strong>CGPA:</strong>

                        {{ student.cgpa }}

                    </p>



                    <p>

                        <strong>10th Marks:</strong>

                        {{ student.tenth_marks }}

                    </p>



                    <p>

                        <strong>12th Marks:</strong>

                        {{ student.twelfth_marks }}

                    </p>



                    <p>

                        <strong>Skills:</strong>

                        {{ student.skills }}

                    </p>



                    <p>

                        <strong>Graduation Year:</strong>

                        {{ student.graduation_year }}

                    </p>



                    <p>

                        <strong>Status:</strong>

                        <span
                            class="badge ms-2"
                            :class="student.profile_completed ? 'bg-success' : 'bg-warning'"
                        >
                            {{ student.profile_completed ? "Profile Complete" : "Incomplete Profile" }}
                        </span>

                    </p>


                </div>



            </div>



            <hr>



            <a

                v-if="student.resume_url"

                :href="student.resume_url"

                target="_blank"

                class="btn btn-primary"

            >

                <i class="bi bi-file-earmark-pdf me-2"></i>

                Download Resume


            </a>
            <p v-else class="text-muted">

                Resume not uploaded

            </p>




            </AdminSectionCard>



        </div>


    </div>


</div>



</template>




<style scoped>


.admin-layout{

    display:flex;

    min-height:100vh;

    background:#f8fafc;

}


.admin-content{

    flex:1;

}


.container-fluid{

    padding:25px;

}



p{

    font-size:16px;

    margin-bottom:15px;

}



</style>