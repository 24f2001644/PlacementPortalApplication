<script setup>

import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"

import StudentSidebar from "../../components/student/StudentSidebar.vue"
import StudentNavbar from "../../components/student/StudentNavbar.vue"
import StudentPageHeader from "../../components/student/StudentPageHeader.vue"
import StudentSectionCard from "../../components/student/StudentSectionCard.vue"
import StudentTableCard from "../../components/student/StudentTableCard.vue"
import StudentLoading from "../../components/student/StudentLoading.vue"
import StudentEmptyState from "../../components/student/StudentEmptyState.vue"

import {

    getDrives

} from "../../services/student"



const router = useRouter()

const loading = ref(true)

const search = ref("")

const drives = ref([])



async function loadDrives(){

    loading.value = true

    try{

        drives.value = await getDrives(

            search.value

        )

    }

    catch(error){

        console.error(error)

        alert("Unable to load placement drives")

    }

    finally{

        loading.value = false

    }

}



function openDrive(id){


    router.push(`/student/drives/${id}`)

}



onMounted(loadDrives)

</script>
<template>

<div class="student-layout">

    <StudentSidebar />

    <div class="student-content">

        <StudentNavbar />

        <div class="container-fluid mt-4">

            <StudentPageHeader

                title="Placement Drives"

                subtitle="Browse and apply for available placement opportunities"

            />



            <StudentLoading

                v-if="loading"

            />



            <template v-else>

                <!-- Search -->

                <StudentSectionCard

                    title="Search Placement Drives"

                >

                    <div class="row align-items-center">

                        <div class="col-md-10">

                            <input

                                type="text"

                                class="form-control"

                                placeholder="Search by role or location..."

                                v-model="search"

                                @keyup.enter="loadDrives"

                            >

                        </div>

                        <div class="col-md-2">

                            <button

                                class="btn btn-primary w-100"

                                @click="loadDrives"

                            >

                                <i class="bi bi-search me-2"></i>

                                Search

                            </button>

                        </div>

                    </div>

                </StudentSectionCard>





                <!-- Drives Table -->

                <StudentTableCard

                    title="Available Placement Drives"

                >

                    <table

                        class="table table-hover align-middle"

                        v-if="drives.length"

                    >

                        <thead>

                            <tr>

                                <th>

                                    Company

                                </th>

                                <th>

                                    Role

                                </th>

                                <th>

                                    Package

                                </th>

                                <th>

                                    Location

                                </th>

                                <th>

                                    Deadline

                                </th>

                                <th>

                                    Action

                                </th>

                            </tr>

                        </thead>





                        <tbody>

                            <tr

                                v-for="drive in drives"

                                :key="drive.drive_id"

                            >

                                <td>

                                    {{ drive.company_name }}

                                </td>

                                <td>

                                    {{ drive.job_title }}

                                </td>

                                <td>

                                    {{ drive.salary_package }}

                                </td>

                                <td>

                                    {{ drive.interview_location }}

                                </td>

                                <td>

                                    {{ drive.application_deadline }}

                                </td>

                                <td>

                                    <button

                                        class="btn btn-outline-primary btn-sm"

                                        @click="openDrive(drive.drive_id)"

                                    >

                                        <i class="bi bi-eye me-1"></i>

                                        View

                                    </button>

                                </td>

                            </tr>

                        </tbody>

                    </table>





                    <StudentEmptyState

                        v-else

                        title="No Drives Found"

                        message="There are currently no placement drives available."

                        icon="bi bi-briefcase"

                    />

                </StudentTableCard>

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



.table thead th{

    background:#F1F5F9;

    color:#334155;

    font-weight:700;

    border-bottom:none;

    padding:15px;

}



.table tbody td{

    padding:15px;

    vertical-align:middle;

    color:#475569;

}



.table tbody tr{

    transition:.25s;

}



.table tbody tr:hover{

    background:#F8FAFC;

}



.form-control{

    border-radius:12px;

    border:1px solid #CBD5E1;

    padding:11px 15px;

}



.form-control:focus{

    border-color:#0EA5E9;

    box-shadow:0 0 0 .2rem rgba(14,165,233,.15);

}



.btn{

    border-radius:10px;

    font-weight:600;

}



.btn-outline-primary{

    border-width:2px;

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



    .table{

        font-size:14px;

    }



    .btn{

        width:100%;

    }

}

</style>