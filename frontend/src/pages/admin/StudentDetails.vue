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

    id:"",

    name:"",

    roll:"",

    email:"",

    phone:"",

    course:"",

    branch:"",

    cgpa:"",

    tenth:"",

    twelfth:"",

    skills:"",

    grad:"",

    resume:""

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

                        {{ student.name }}

                    </p>


                    <p>

                        <strong>Roll Number:</strong>

                        {{ student.roll }}

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

                        {{ student.tenth }}

                    </p>



                    <p>

                        <strong>12th Marks:</strong>

                        {{ student.twelfth }}

                    </p>



                    <p>

                        <strong>Skills:</strong>

                        {{ student.skills }}

                    </p>



                    <p>

                        <strong>Graduation Year:</strong>

                        {{ student.grad }}

                    </p>



                    <p>

                        <strong>Status:</strong>

                        <span class="badge bg-success ms-2">

                            Profile Complete

                        </span>

                    </p>


                </div>



            </div>



            <hr>



            <a

                :href="student.resume"

                target="_blank"

                class="btn btn-primary"

            >

                <i class="bi bi-file-earmark-pdf me-2"></i>

                Download Resume


            </a>




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