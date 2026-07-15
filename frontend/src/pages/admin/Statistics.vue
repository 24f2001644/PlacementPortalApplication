<script setup>

import { 
    ref, 
    computed, 
    onMounted 
} from "vue"


import AdminSidebar from "../../components/admin/AdminSidebar.vue"
import AdminNavbar from "../../components/admin/AdminNavbar.vue"
import AdminPageHeader from "../../components/admin/AdminPageHeader.vue"

import AdminStatsCard from "../../components/admin/AdminStatsCard.vue"
import AdminSectionCard from "../../components/admin/AdminSectionCard.vue"
import AdminTableCard from "../../components/admin/AdminTableCard.vue"

import AdminLoading from "../../components/admin/AdminLoading.vue"
import AdminEmptyState from "../../components/admin/AdminEmptyState.vue"

import AdminBarChart from "../../components/admin/AdminBarChart.vue"
import AdminPieChart from "../../components/admin/AdminPieChart.vue"
import AdminProgressCard from "../../components/admin/AdminProgressCard.vue"


import {
    getStatistics
}
from "../../services/admin"



const loading = ref(true)



const statistics = ref({

    total_students:0,

    active_students:0,

    blocked_students:0,


    total_companies:0,

    approved_companies:0,

    pending_companies:0,


    total_drives:0,

    approved_drives:0,

    pending_drives:0,


    total_applications:0,


    applied:0,

    shortlisted:0,

    selected:0,

    rejected:0,


    placement_percentage:0,


    branch_statistics:[],

    company_statistics:[],

    monthly_registrations:[]

})





/*
==========================================
CARDS
==========================================
*/


const cards = computed(()=>[


{
    title:"Students",
    value:statistics.value.total_students,
    color:"primary",
    icon:"bi bi-people-fill"
},


{
    title:"Active Students",
    value:statistics.value.active_students,
    color:"success",
    icon:"bi bi-person-check-fill"
},


{
    title:"Companies",
    value:statistics.value.total_companies,
    color:"warning",
    icon:"bi bi-building"
},


{
    title:"Placement Drives",
    value:statistics.value.total_drives,
    color:"info",
    icon:"bi bi-briefcase-fill"
},


{
    title:"Applications",
    value:statistics.value.total_applications,
    color:"secondary",
    icon:"bi bi-file-earmark-text"
},


{
    title:"Selected Students",
    value:statistics.value.selected,
    color:"success",
    icon:"bi bi-award-fill"
},


{
    title:"Placement %",
    value:statistics.value.placement_percentage+"%",
    color:"danger",
    icon:"bi bi-graph-up"
},


{
    title:"Approved Companies",
    value:statistics.value.approved_companies,
    color:"primary",
    icon:"bi bi-patch-check"
}


])





/*
==========================================
BAR CHART DATA
==========================================
*/


const branchChart = computed(()=>{


return {


labels:

statistics.value.branch_statistics.map(
    item=>item.branch
),


values:

statistics.value.branch_statistics.map(
    item=>item.students
)


}


})





/*
==========================================
APPLICATION PIE DATA
==========================================
*/


const applicationChart = computed(()=>{


return {


labels:[

"Applied",

"Shortlisted",

"Selected",

"Rejected"

],


values:[

statistics.value.applied,

statistics.value.shortlisted,

statistics.value.selected,

statistics.value.rejected

]


}


})






async function loadStatistics(){

    loading.value=true

    try{

        const response = await getStatistics()


        statistics.value = {

            ...statistics.value,

            ...response

        }


    }

    catch(error){

        console.error(error)

        alert(
            "Unable to load statistics"
        )

    }

    finally{

        loading.value=false

    }

}




onMounted(loadStatistics)



</script>





<template>


<div class="admin-layout">


    <AdminSidebar/>


    <div class="admin-content">


        <AdminNavbar/>



        <div class="container-fluid p-4">



            <AdminPageHeader

                title="Placement Statistics"

                subtitle="Overall placement analytics"

            />




            <AdminLoading

                v-if="loading"

            />




            <template v-else>



                <!-- CARDS -->

                <div class="row g-4 mb-4">


                    <div

                    v-for="card in cards"

                    :key="card.title"

                    class="col-xl-3 col-lg-4 col-md-6"

                    >


                        <AdminStatsCard

                            :title="card.title"

                            :value="card.value"

                            :color="card.color"

                            :icon="card.icon"

                        />


                    </div>


                </div>






                <!-- CHARTS -->


                <div class="row g-4 mb-4">



                    <div class="col-lg-6">


                        <AdminSectionCard

                            title="Students By Branch"

                        >



                            <AdminBarChart


                                v-if="
                                branchChart.labels.length
                                "


                                :labels="
                                branchChart.labels
                                "


                                :values="
                                branchChart.values
                                "


                            />



                            <AdminEmptyState

                                v-else

                                title="No Branch Data"

                                description=
                                "No student branch information available"

                            />



                        </AdminSectionCard>


                    </div>






                    <div class="col-lg-6">


                        <AdminSectionCard

                            title="Application Status"

                        >



                            <AdminPieChart


                                :labels="
                                applicationChart.labels
                                "


                                :values="
                                applicationChart.values
                                "


                            />



                        </AdminSectionCard>



                    </div>



                </div>








                <!-- PROGRESS -->

                <div class="row g-4 mb-4">



                    <div class="col-lg-6">


                        <AdminProgressCard

                            title="Placement Rate"

                            label="Students Placed"

                            :value="statistics.selected || 0"

                            :total="statistics.total_students || 0"

                            color="success"

                        />


                    </div>




                    <div class="col-lg-6">


                        <AdminProgressCard

                            title="Company Approval"

                            label="Approved Companies"

                            :value="statistics.approved_companies || 0"

                            :total="statistics.total_companies || 0"

                            color="primary"

                        />


                    </div>


                </div>








                <!-- COMPANY TABLE -->


                <AdminTableCard

                    title="Company Hiring Statistics"

                >



                <table class="table table-hover">


                    <thead>


                        <tr>

                            <th>
                                Company
                            </th>


                            <th>
                                Drives
                            </th>


                            <th>
                                Selected Students
                            </th>


                        </tr>


                    </thead>



                    <tbody>



                    <tr

                    v-for="company in statistics.company_statistics"

                    :key="company.company_name"

                    >


                        <td>
                            {{company.company_name}}
                        </td>


                        <td>
                            {{company.total_drives}}
                        </td>


                        <td>
                            {{company.selected_students}}
                        </td>



                    </tr>



                    <tr

                    v-if="
                    statistics.company_statistics.length===0
                    "

                    >

                        <td
                        colspan="3"
                        class="text-center"
                        >

                            No Company Data

                        </td>


                    </tr>


                    </tbody>


                </table>


                </AdminTableCard>





            </template>



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



.table{

margin-bottom:0;

}



.table th{

background:#f1f5f9;

font-weight:700;

}



</style>