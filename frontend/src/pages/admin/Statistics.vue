<script setup>

import { ref, computed, onMounted } from "vue"

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

} from "../../services/admin"

const loading = ref(true)

const statistics = ref({

    total_students: 0,

    eligible_students: 0,

    companies: 0,

    active_drives: 0,

    applications: 0,

    placed_students: 0,

    placement_percentage: 0,

    highest_package: 0,

    average_package: 0,

    branches: [],

    recent_activity: []

})

/* =========================================
   Statistics Cards
========================================= */

const cards = computed(() => [

    {

        title: "Students",

        value: statistics.value.total_students,

        color: "primary",

        icon: "bi bi-people-fill"

    },

    {

        title: "Eligible",

        value: statistics.value.eligible_students,

        color: "success",

        icon: "bi bi-person-check-fill"

    },

    {

        title: "Companies",

        value: statistics.value.companies,

        color: "warning",

        icon: "bi bi-buildings"

    },

    {

        title: "Active Drives",

        value: statistics.value.active_drives,

        color: "info",

        icon: "bi bi-briefcase-fill"

    },

    {

        title: "Applications",

        value: statistics.value.applications,

        color: "secondary",

        icon: "bi bi-file-earmark-text-fill"

    },

    {

        title: "Placed",

        value: statistics.value.placed_students,

        color: "success",

        icon: "bi bi-award-fill"

    },

    {

        title: "Placement %",

        value: statistics.value.placement_percentage + "%",

        color: "danger",

        icon: "bi bi-graph-up-arrow"

    },

    {

        title: "Highest Package",

        value: statistics.value.highest_package,

        color: "primary",

        icon: "bi bi-cash-stack"

    }

])

async function loadStatistics(){

    loading.value = true

    try{

        statistics.value = await getStatistics()

    }

    catch(error){

        console.error(error)

        alert("Unable to load statistics")

    }

    finally{

        loading.value = false

    }

}

onMounted(loadStatistics)

</script>


<template>

<div class="admin-layout">


    <!-- Sidebar -->

    <AdminSidebar />


    <div class="admin-content">


        <!-- Navbar -->

        <AdminNavbar />


        <div class="container-fluid mt-4">


            <!-- Page Header -->

            <AdminPageHeader

                title="Placement Statistics"

                subtitle="Overview of placement activities, students and companies"

            />



            <!-- Loading -->

            <AdminLoading

                v-if="loading"

            />



            <template v-else>



                <!-- Statistics Cards -->

                <div class="row g-3 mb-4">


                    <div

                        class="col-md-3"

                        v-for="card in cards"

                        :key="card.title"

                    >


                        <AdminStatsCard

                            :title="card.title"

                            :value="card.value"

                            :color="card.color"

                            :icon="card.icon"

                        />


                    </div>


                </div>





                <!-- Charts Section -->


                <div class="row g-4 mb-4">



                    <!-- Branch Wise Students -->


                    <div class="col-md-6">


                        <AdminSectionCard

                            title="Students By Branch"

                        >


                            <AdminBarChart

                                :data="statistics.branches"

                            />


                        </AdminSectionCard>


                    </div>





                    <!-- Placement Distribution -->


                    <div class="col-md-6">


                        <AdminSectionCard

                            title="Placement Distribution"

                        >


                            <AdminPieChart

                                :placed="statistics.placed_students"

                                :total="statistics.total_students"

                            />


                        </AdminSectionCard>


                    </div>



                </div>







                <!-- Package Information -->


                <div class="row g-4 mb-4">


                    <div class="col-md-6">


                        <AdminProgressCard

                            title="Placement Rate"

                            label="Students Placed"

                            :value="statistics.placement_percentage"

                        />


                    </div>




                    <div class="col-md-6">


                        <AdminProgressCard

                            title="Average Package"

                            label="Average Salary"

                            :value="statistics.average_package"

                        />


                    </div>


                </div>







                <!-- Recent Activity -->


                <AdminTableCard

                    title="Recent Placement Activity"


                >


                    <table

                        class="table table-hover"

                    >


                        <thead>


                            <tr>


                                <th>

                                    Activity

                                </th>


                                <th>

                                    Date

                                </th>


                                <th>

                                    Status

                                </th>


                            </tr>


                        </thead>



                        <tbody>



                            <tr

                                v-for="item in statistics.recent_activity"

                                :key="item.id"

                            >


                                <td>

                                    {{ item.message }}

                                </td>



                                <td>

                                    {{ item.date }}

                                </td>



                                <td>


                                    <span

                                        class="badge bg-success"

                                    >

                                        {{ item.status }}

                                    </span>


                                </td>


                            </tr>



                            <tr

                                v-if="statistics.recent_activity.length===0"

                            >


                                <td

                                    colspan="3"

                                    class="text-center"

                                >


                                    <AdminEmptyState

                                        message="No recent activities"

                                    />


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

    background:#f8f9fa;

}



.admin-content{

    flex:1;

}



.container-fluid{

    padding-left:25px;

    padding-right:25px;

}




.card{

    border-radius:15px;

}



.table{

    margin-bottom:0;

}



.badge{

    padding:8px 12px;

    border-radius:20px;

}




@media(max-width:768px){


    .admin-content{

        margin-left:0;

    }


}



</style>