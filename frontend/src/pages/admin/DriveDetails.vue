<script setup>

import { ref, reactive, computed, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"

import AdminSidebar from "../../components/admin/AdminSidebar.vue"
import AdminNavbar from "../../components/admin/AdminNavbar.vue"
import AdminPageHeader from "../../components/admin/AdminPageHeader.vue"
import AdminSectionCard from "../../components/admin/AdminSectionCard.vue"
import AdminStatsCard from "../../components/admin/AdminStatsCard.vue"
import AdminTableCard from "../../components/admin/AdminTableCard.vue"
import AdminBadge from "../../components/admin/AdminBadge.vue"
import AdminButton from "../../components/admin/AdminButton.vue"
import AdminEmptyState from "../../components/admin/AdminEmptyState.vue"
import AdminLoading from "../../components/admin/AdminLoading.vue"

import {

    getDriveDetails,

    closeDrive

} from "../../services/admin"

const route = useRoute()

const router = useRouter()

const loading = ref(true)

const drive = reactive({

    drive_id: null,

    company_name: "",

    job_title: "",

    job_description: "",

    salary_package: "",

    eligible_cgpa: "",

    eligible_branches: "",

    application_deadline: "",

    interview_date: "",

    interview_location: "",

    status: "",

    applicants: []

})

const stats = computed(() => ({

    totalApplicants:

        drive.applicants.length,

    selected:

        drive.applicants.filter(

            a => a.status === "Selected"

        ).length,

    shortlisted:

        drive.applicants.filter(

            a => a.status === "Shortlisted"

        ).length,

    rejected:

        drive.applicants.filter(

            a => a.status === "Rejected"

        ).length

}))

async function loadDrive(){

    loading.value = true

    try{

        const data = await getDriveDetails(

            route.params.id

        )

        Object.assign(

            drive,

            data

        )

    }

    catch(error){

        console.error(error)

        alert("Unable to load placement drive.")

    }

    finally{

        loading.value = false

    }

}

async function closePlacementDrive(){

    if(

        !confirm(

            "Close this placement drive?"

        )

    ){

        return

    }

    try{

        await closeDrive(

            drive.drive_id

        )

        await loadDrive()

    }

    catch(error){

        console.error(error)

        alert("Unable to close drive.")

    }

}

function deletePlacementDrive(){

    alert(

        "Delete API not implemented yet."

    )

}

function badgeType(status){

    switch(status){

        case "Selected":

        case "Approved":

            return "success"

        case "Shortlisted":

        case "Pending":

            return "warning"

        case "Rejected":

            return "danger"

        case "Closed":

            return "secondary"

        default:

            return "primary"

    }

}

onMounted(

    loadDrive

)

</script>


<template>

<div class="admin-layout">

    <AdminSidebar />

    <div class="admin-content">

        <AdminNavbar />

        <div class="container-fluid p-4">

            <AdminPageHeader

                title="Placement Drive Details"

                subtitle="View complete information and manage applicants"

            />

            <AdminLoading v-if="loading" />

            <template v-else>

                <!-- ===================================== -->
                <!-- Statistics -->
                <!-- ===================================== -->

                <div class="row g-4 mb-4">

                    <div class="col-xl-3 col-md-6">

                        <AdminStatsCard

                            title="Applicants"

                            :value="stats.totalApplicants"

                            subtitle="Total Applications"

                            color="primary"

                            icon="bi bi-people-fill"

                        />

                    </div>

                    <div class="col-xl-3 col-md-6">

                        <AdminStatsCard

                            title="Selected"

                            :value="stats.selected"

                            subtitle="Final Selected"

                            color="success"

                            icon="bi bi-check-circle-fill"

                        />

                    </div>

                    <div class="col-xl-3 col-md-6">

                        <AdminStatsCard

                            title="Shortlisted"

                            :value="stats.shortlisted"

                            subtitle="Interview Round"

                            color="warning"

                            icon="bi bi-award-fill"

                        />

                    </div>

                    <div class="col-xl-3 col-md-6">

                        <AdminStatsCard

                            title="Rejected"

                            :value="stats.rejected"

                            subtitle="Not Selected"

                            color="danger"

                            icon="bi bi-x-circle-fill"

                        />

                    </div>

                </div>

                <!-- ===================================== -->
                <!-- Drive Information -->
                <!-- ===================================== -->

                <div class="row g-4">

                    <!-- Left Card -->

                    <div class="col-lg-8">

                        <AdminSectionCard

                            title="Job Information"

                            icon="bi bi-briefcase-fill"

                        >

                            <div class="mb-3">

                                <h2 class="fw-bold mb-1">

                                    {{ drive.job_title }}

                                </h2>

                                <p class="mt-3 text-muted">

                                    {{ drive.job_description }}

                                </p>

                                <p class="text-muted mb-0">

                                    {{ drive.company_name }}

                                </p>

                            </div>

                            <hr>

                            <div class="row gy-4">

                                <div class="col-md-6">

                                    <label class="text-muted small">

                                        Salary Package

                                    </label>

                                    <h6 class="fw-bold">

                                        {{ drive.salary_package }}

                                    </h6>

                                </div>

                                <div class="col-md-6">

                                    <label class="text-muted small">

                                        Minimum CGPA

                                    </label>

                                    <h6 class="fw-bold">

                                        {{ drive.eligible_cgpa }}

                                    </h6>

                                </div>

                                <div class="col-md-6">

                                    <label class="text-muted small">

                                        Eligible Branches

                                    </label>

                                    <h6 class="fw-bold">

                                        {{ drive.eligible_branches }}

                                    </h6>

                                </div>

                                <div class="col-md-6">

                                    <label class="text-muted small">

                                        Application Deadline

                                    </label>

                                    <h6 class="fw-bold">

                                        {{ drive.application_deadline }}

                                    </h6>

                                </div>

                                <div class="col-md-6">

                                    <label class="text-muted small">

                                        Interview Date

                                    </label>

                                    <h6 class="fw-bold">

                                        {{ drive.interview_date || "Not Scheduled" }}

                                    </h6>

                                </div>

                                <div class="col-md-6">

                                    <label class="text-muted small">

                                        Interview Location

                                    </label>

                                    <h6 class="fw-bold">

                                        {{ drive.interview_location || "TBA" }}

                                    </h6>

                                </div>

                            </div>

                        </AdminSectionCard>

                    </div>

                    <!-- Right Card -->

                    <div class="col-lg-4">

                        <AdminSectionCard title="Drive Status">

                            <div class="text-center mb-4">
                                <AdminBadge
                                    :label="drive.status"
                                    :type="badgeType(drive.status)"
                                />
                            </div>

                            <div class="row gy-3">

                                <div class="col-12">
                                    <small class="text-muted">Applications</small>
                                    <h6>{{ drive.total_applications }}</h6>
                                </div>

                                <div class="col-12">
                                    <small class="text-muted">Created On</small>
                                    <h6>{{ drive.created_at }}</h6>
                                </div>

                            </div>

                        </AdminSectionCard>

                    </div>

                </div>

                <!-- ===================================== -->
                <!-- Applicants -->
                <!-- ===================================== -->

                <div class="row mt-4">

                    <div class="col-12">

                        <AdminTableCard

                            title="Applicants"

                            icon="bi bi-people-fill"

                        >

                            <template
                                v-if="drive.applicants.length"
                            >

                                <div class="table-responsive">

                                    <table class="table admin-table align-middle">

                                        <thead>

                                            <tr>

                                                <th>Student</th>

                                                <th>Roll No.</th>

                                                <th>Branch</th>

                                                <th>CGPA</th>

                                                <th>Status</th>

                                                <th>Applied On</th>

                                            </tr>

                                        </thead>

                                        <tbody>

                                            <tr

                                                v-for="student in drive.applicants"

                                                :key="student.application_id"

                                            >

                                                <td>

                                                    <div class="fw-semibold">

                                                        {{ student.full_name }}

                                                    </div>

                                                </td>

                                                <td>

                                                    {{ student.roll_number }}

                                                </td>

                                                <td>

                                                    {{ student.branch }}

                                                </td>

                                                <td>

                                                    {{ student.cgpa }}

                                                </td>

                                                <td>

                                                    <AdminBadge

                                                        :label="student.status"

                                                        :type="badgeType(student.status)"

                                                    />

                                                </td>

                                                <td>

                                                    {{ student.application_date }}

                                                </td>

                                            </tr>

                                        </tbody>

                                    </table>

                                </div>

                            </template>

                            <template v-else>

                                <AdminEmptyState

                                    icon="bi bi-inbox"

                                    title="No Applicants Yet"

                                    description="Students who apply for this placement drive will appear here."

                                />

                            </template>

                        </AdminTableCard>

                    </div>

                </div>

            </template>

        </div>

    </div>

</div>

</template>

<style scoped>

.admin-layout{

    display:flex;

    min-height:100vh;

    background:#f5f7fb;

}

.admin-content{

    flex:1;

    overflow-x:hidden;

}

.admin-table{

    margin:0;

}

.admin-table thead th{

    background:#eef2ff;

    color:#5b5fc7;

    font-weight:700;

    border:none;

    padding:16px;

    white-space:nowrap;

}

.admin-table tbody td{

    padding:16px;

    border-top:1px solid #edf2f7;

    vertical-align:middle;

}

.admin-table tbody tr{

    transition:.25s ease;

}

.admin-table tbody tr:hover{

    background:#f8faff;

    transform:scale(1.003);

}

.table-responsive{

    border-radius:18px;

    overflow:hidden;

}

@media(max-width:992px){

    .admin-layout{

        flex-direction:column;

    }

}

@media(max-width:768px){

    .admin-table{

        font-size:14px;

    }

}

</style>