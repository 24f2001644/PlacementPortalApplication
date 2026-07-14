<script setup>

import { ref, onMounted } from "vue"

import StudentSidebar from "../../components/student/StudentSidebar.vue"
import StudentNavbar from "../../components/student/StudentNavbar.vue"
import StudentPageHeader from "../../components/student/StudentPageHeader.vue"
import StudentTableCard from "../../components/student/StudentTableCard.vue"
import StudentLoading from "../../components/student/StudentLoading.vue"
import StudentEmptyState from "../../components/student/StudentEmptyState.vue"

import {

    getApplications,

    withdrawApplication

} from "../../services/student"



const loading = ref(true)

const applications = ref([])



async function loadApplications(){

    loading.value = true

    try{

        applications.value = await getApplications()

    }

    catch(error){

        console.error(error)

        alert("Unable to load applications")

    }

    finally{

        loading.value = false

    }

}



async function withdraw(id){

    if(

        !confirm(

            "Are you sure you want to withdraw this application?"

        )

    ){

        return

    }



    try{

        await withdrawApplication(id)

        await loadApplications()

        alert("Application withdrawn successfully")

    }

    catch(error){

        console.error(error)

        alert(

            error.response?.data?.message ||

            "Unable to withdraw application"

        )

    }

}



function badgeClass(status){

    switch(status){

        case "Applied":

            return "bg-primary"

        case "Shortlisted":

            return "bg-warning"

        case "Selected":

            return "bg-success"

        case "Rejected":

            return "bg-danger"

        default:

            return "bg-secondary"

    }

}



onMounted(loadApplications)

</script>

<template>

<div class="student-layout">

    <StudentSidebar />

    <div class="student-content">

        <StudentNavbar />

        <div class="container-fluid mt-4">

            <StudentPageHeader

                title="My Applications"

                subtitle="Track the status of all your placement applications"

            />



            <StudentLoading

                v-if="loading"

            />



            <template v-else>

                <StudentTableCard

                    title="Application History"

                >

                    <table

                        class="table table-hover align-middle"

                        v-if="applications.length"

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

                                    Applied On

                                </th>

                                <th>

                                    Status

                                </th>

                                <th>

                                    Action

                                </th>

                            </tr>

                        </thead>



                        <tbody>

                            <tr

                                v-for="application in applications"

                                :key="application.application_id"

                            >

                                <td>

                                    {{ application.company_name }}

                                </td>

                                <td>

                                    {{ application.job_title }}

                                </td>

                                <td>

                                    {{ application.application_date }}

                                </td>

                                <td>

                                    <span

                                        class="badge"

                                        :class="badgeClass(application.status)"

                                    >

                                        {{ application.status }}

                                    </span>

                                </td>

                                <td>

                                    <button

                                        v-if="application.status==='Applied'"

                                        class="btn btn-outline-danger btn-sm"

                                        @click="withdraw(application.application_id)"

                                    >

                                        <i class="bi bi-trash me-1"></i>

                                        Withdraw

                                    </button>

                                    <span

                                        v-else

                                        class="text-muted"

                                    >

                                        --

                                    </span>

                                </td>

                            </tr>

                        </tbody>

                    </table>



                    <StudentEmptyState

                        v-else

                        title="No Applications"

                        message="You haven't applied for any placement drives yet."

                        icon="bi bi-file-earmark-text"

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



.badge{

    padding:8px 14px;

    border-radius:20px;

    font-size:13px;

    font-weight:600;

}



.btn{

    border-radius:10px;

    font-weight:600;

}



.btn-outline-danger{

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