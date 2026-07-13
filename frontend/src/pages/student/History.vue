<script setup>

import { ref, computed, onMounted } from "vue"

import StudentSidebar from "../../components/student/StudentSidebar.vue"
import StudentNavbar from "../../components/student/StudentNavbar.vue"
import StudentPageHeader from "../../components/student/StudentPageHeader.vue"
import StudentTableCard from "../../components/student/StudentTableCard.vue"
import StudentLoading from "../../components/student/StudentLoading.vue"
import StudentEmptyState from "../../components/student/StudentEmptyState.vue"

import {

    getApplications

} from "../../services/student"



const loading = ref(true)

const applications = ref([])



const history = computed(()=>{

    return applications.value.filter(

        application =>

            application.status==="Selected" ||

            application.status==="Rejected" ||

            application.status==="Shortlisted"

    )

})



async function loadHistory(){

    loading.value = true

    try{

        applications.value = await getApplications()

    }

    catch(error){

        console.error(error)

        alert("Unable to load history")

    }

    finally{

        loading.value = false

    }

}



function badgeClass(status){

    switch(status){

        case "Selected":

            return "bg-success"

        case "Rejected":

            return "bg-danger"

        case "Shortlisted":

            return "bg-warning"

        default:

            return "bg-secondary"

    }

}



onMounted(loadHistory)

</script>
<template>

<div class="student-layout">

    <StudentSidebar />

    <div class="student-content">

        <StudentNavbar />

        <div class="container-fluid mt-4">

            <StudentPageHeader

                title="Placement History"

                subtitle="View the outcomes of your placement applications"

            />



            <StudentLoading

                v-if="loading"

            />



            <template v-else>

                <StudentTableCard

                    title="Placement Results"

                >

                    <table

                        class="table table-hover align-middle"

                        v-if="history.length"

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

                                    Result

                                </th>

                            </tr>

                        </thead>



                        <tbody>

                            <tr

                                v-for="application in history"

                                :key="application.application_id"

                            >

                                <td>

                                    {{ application.company }}

                                </td>

                                <td>

                                    {{ application.role }}

                                </td>

                                <td>

                                    {{ application.applied_date }}

                                </td>

                                <td>

                                    <span

                                        class="badge"

                                        :class="badgeClass(application.status)"

                                    >

                                        {{ application.status }}

                                    </span>

                                </td>

                            </tr>

                        </tbody>

                    </table>



                    <StudentEmptyState

                        v-else

                        title="No Placement History"

                        message="Your completed placement results will appear here."

                        icon="bi bi-clock-history"

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

}

</style>