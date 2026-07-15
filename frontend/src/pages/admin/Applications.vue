<script setup>

import { ref, computed, onMounted } from "vue"


import AdminSidebar from "../../components/admin/AdminSidebar.vue"
import AdminNavbar from "../../components/admin/AdminNavbar.vue"
import AdminPageHeader from "../../components/admin/AdminPageHeader.vue"
import AdminTableCard from "../../components/admin/AdminTableCard.vue"
import AdminSearchBar from "../../components/admin/AdminSearchBar.vue"
import AdminFilterBar from "../../components/admin/AdminFilterBar.vue"
import AdminBadge from "../../components/admin/AdminBadge.vue"
import AdminButton from "../../components/admin/AdminButton.vue"
import AdminLoading from "../../components/admin/AdminLoading.vue"
import AdminEmptyState from "../../components/admin/AdminEmptyState.vue"


import {
    getApplications,
    updateApplicationStatus
}
from "../../services/admin"



const loading = ref(false)

const search = ref("")

const status = ref("")

const applications = ref([])



const statusOptions=[

    "Applied",
    "Shortlisted",
    "Selected",
    "Rejected"

]




async function loadApplications(){


    loading.value=true


    try{


        applications.value = await getApplications(
            search.value,
            status.value
        )


    }

    catch(error){

        console.error(error)

        alert("Unable to load applications")

    }


    finally{

        loading.value=false

    }


}





function handleSearch(value){

    search.value=value

    loadApplications()

}




function handleFilter(data){


    status.value=data.status || ""

    search.value=data.search || ""

    loadApplications()


}




const filteredApplications=computed(()=>{


    return applications.value


})





async function approve(app){


    try{


        await updateApplicationStatus(

            app.application_id,

            "Selected"

        )


        await loadApplications()


    }

    catch(error){

        console.error(error)

        alert("Unable to update application")

    }


}





async function reject(app){


    try{


        await updateApplicationStatus(

            app.application_id,

            "Rejected"

        )


        await loadApplications()


    }

    catch(error){

        console.error(error)

        alert("Unable to update application")

    }


}




function getStatusColor(status){


    if(status==="Selected")
        return "success"


    if(status==="Rejected")
        return "danger"


    if(status==="Shortlisted")
        return "warning"


    return "primary"


}




onMounted(loadApplications)


</script>




<template>


<div class="admin-layout">


    <AdminSidebar/>


    <div class="admin-content">


        <AdminNavbar/>



        <div class="container-fluid page-padding">


            <AdminPageHeader

                title="Applications"

                subtitle="Manage placement applications"

            />



            <AdminTableCard>




                <div class="toolbar">


                    <div class="search-area">


                        <AdminSearchBar

                            placeholder="Search Student, Company, Role"

                            @search="handleSearch"

                        />


                    </div>



                    <div class="filter-area">


                        <AdminFilterBar

                            :options="statusOptions"

                            @filter="handleFilter"

                        />


                    </div>



                </div>





                <AdminLoading

                    v-if="loading"

                />




                <AdminEmptyState

                    v-else-if="filteredApplications.length===0"

                    title="No Applications Found"

                    description="No applications match your search."

                    icon="bi bi-file-earmark-text"

                />





                <table

                    v-else

                    class="table table-hover"

                >



                    <thead>

                    <tr>

                        <th>
                            Student
                        </th>


                        <th>
                            Company
                        </th>


                        <th>
                            Role
                        </th>


                        <th>
                            Status
                        </th>


                        <th class="text-center">
                            Actions
                        </th>


                    </tr>


                    </thead>




                    <tbody>



                    <tr

                    v-for="app in filteredApplications"

                    :key="app.application_id"

                    >



                        <td>

                            <strong>

                                {{app.student_name}}

                            </strong>

                        </td>



                        <td>

                            {{app.company_name}}

                        </td>



                        <td>

                            {{app.job_title}}

                        </td>




                        <td>


                            <AdminBadge

                                :label="app.status"

                                :type="getStatusColor(app.status)"

                            />


                        </td>




                        <td>


                            <div class="actions">


                                <AdminButton

                                    v-if="app.status!=='Selected'"

                                    text="Select"

                                    color="success"

                                    icon="bi bi-check-circle"

                                    @click="approve(app)"

                                />



                                <AdminButton

                                    v-if="app.status!=='Rejected'"

                                    text="Reject"

                                    color="danger"

                                    icon="bi bi-x-circle"

                                    @click="reject(app)"

                                />


                            </div>


                        </td>




                    </tr>



                    </tbody>



                </table>




            </AdminTableCard>



        </div>



    </div>



</div>



</template>




<style scoped>


.admin-layout{

    display:flex;

    min-height:100vh;

    background:#f4f7fb;

}



.admin-content{

    flex:1;

}



.page-padding{

    padding:25px;

}



.toolbar{

    display:flex;

    align-items:center;

    gap:20px;

    margin-bottom:25px;

}



.search-area{

    flex:1;

}



.filter-area{

    width:300px;

}




.table{

    margin-bottom:0;

}



.table thead th{

    background:#f8fafc;

    padding:15px;

    font-weight:700;

}



.table tbody td{

    padding:16px;

    vertical-align:middle;

}




.actions{

    display:flex;

    justify-content:center;

    gap:12px;

}



.actions :deep(button){

    min-width:100px;

    height:38px;

    font-weight:600;

    border-radius:8px;

}




@media(max-width:768px){


.toolbar{

    flex-direction:column;

    align-items:stretch;

}



.filter-area{

    width:100%;

}


.actions{

    flex-direction:column;

}


}


</style>