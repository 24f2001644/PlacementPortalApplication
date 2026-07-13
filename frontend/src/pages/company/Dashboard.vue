<script setup>

import { ref, computed, onMounted } from "vue"

import CompanySidebar from "../../components/company/CompanySidebar.vue"
import CompanyNavbar from "../../components/company/CompanyNavbar.vue"
import CompanyPageHeader from "../../components/company/CompanyPageHeader.vue"
import CompanyStatsCard from "../../components/company/CompanyStatsCard.vue"
import CompanySectionCard from "../../components/company/CompanySectionCard.vue"
import CompanyTableCard from "../../components/company/CompanyTableCard.vue"
import CompanyLoading from "../../components/company/CompanyLoading.vue"
import CompanyEmptyState from "../../components/company/CompanyEmptyState.vue"
import CompanyStatusBadge from "../../components/company/CompanyStatusBadge.vue"

import {

    getDashboard

} from "../../services/company"



const loading = ref(true)

const dashboard = ref({

    company_name:"",

    total_drives:0,

    active_drives:0,

    total_applications:0,

    shortlisted:0,

    selected:0,

    recent_applications:[]

})



const cards = computed(()=>([

    {

        title:"Placement Drives",

        value:dashboard.value.total_drives,

        color:"primary",

        icon:"bi bi-briefcase-fill"

    },

    {

        title:"Active Drives",

        value:dashboard.value.active_drives,

        color:"success",

        icon:"bi bi-play-circle-fill"

    },

    {

        title:"Applications",

        value:dashboard.value.total_applications,

        color:"warning",

        icon:"bi bi-file-earmark-text-fill"

    },

    {

        title:"Selected",

        value:dashboard.value.selected,

        color:"info",

        icon:"bi bi-award-fill"

    }

]))



async function loadDashboard(){

    loading.value = true

    try{

        dashboard.value = await getDashboard()

    }

    catch(error){

        console.error(error)

        alert("Unable to load dashboard")

    }

    finally{

        loading.value = false

    }

}



onMounted(

    loadDashboard

)

</script>

<template>

<div class="company-layout">

    <CompanySidebar />

    <div class="company-content">

        <CompanyNavbar />

        <div class="container-fluid mt-4">

            <CompanyPageHeader

                title="Company Dashboard"

                :subtitle="`Welcome ${dashboard.company_name || 'Recruiter'}`"

            />



            <CompanyLoading

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

                        <CompanyStatsCard

                            :title="card.title"

                            :value="card.value"

                            :color="card.color"

                            :icon="card.icon"

                        />

                    </div>

                </div>



                <!-- Summary -->

                <div class="row g-4 mb-4">

                    <div class="col-lg-4">

                        <CompanySectionCard

                            title="Company Summary"

                        >

                            <div class="mb-3">

                                <strong>

                                    Company

                                </strong>

                                <p class="text-muted mb-0">

                                    {{ dashboard.company_name }}

                                </p>

                            </div>



                            <div class="mb-3">

                                <strong>

                                    Active Drives

                                </strong>

                                <p class="text-muted mb-0">

                                    {{ dashboard.active_drives }}

                                </p>

                            </div>



                            <div>

                                <strong>

                                    Shortlisted Students

                                </strong>

                                <p class="text-muted mb-0">

                                    {{ dashboard.shortlisted }}

                                </p>

                            </div>

                        </CompanySectionCard>

                    </div>



                    <div class="col-lg-8">

                        <CompanyTableCard

                            title="Recent Applications"

                        >

                            <table

                                class="table table-hover"

                                v-if="dashboard.recent_applications.length"

                            >

                                <thead>

                                    <tr>

                                        <th>

                                            Student

                                        </th>

                                        <th>

                                            Role

                                        </th>

                                        <th>

                                            Status

                                        </th>

                                    </tr>

                                </thead>



                                <tbody>

                                    <tr

                                        v-for="application in dashboard.recent_applications"

                                        :key="application.id"

                                    >

                                        <td>

                                            {{ application.student }}

                                        </td>

                                        <td>

                                            {{ application.role }}

                                        </td>

                                        <td>

                                            <CompanyStatusBadge

                                                :status="application.status"

                                            />

                                        </td>

                                    </tr>

                                </tbody>

                            </table>



                            <CompanyEmptyState

                                v-else

                                title="No Applications"

                                message="Applications will appear here when students start applying."

                                icon="bi bi-file-earmark-text"

                            />

                        </CompanyTableCard>

                    </div>

                </div>



            </template>

        </div>

    </div>

</div>

</template>

<style scoped>

.company-layout{

    display:flex;

    min-height:100vh;

    background:#F8FAFC;

}



.company-content{

    flex:1;

    display:flex;

    flex-direction:column;

}



.container-fluid{

    padding:28px;

}



.table td{

    vertical-align:middle;

}



.table th{

    font-weight:600;

    color:#475569;

}



.text-muted{

    color:#64748B !important;

}



@media(max-width:992px){

.company-layout{

    flex-direction:column;

}

}



@media(max-width:768px){

.container-fluid{

    padding:18px;

}

}

</style>