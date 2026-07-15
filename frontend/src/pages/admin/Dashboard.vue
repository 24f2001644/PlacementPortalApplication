<script setup>

import { ref, computed, onMounted } from "vue"

import AdminSidebar from "../../components/admin/AdminSidebar.vue"
import AdminNavbar from "../../components/admin/AdminNavbar.vue"
import AdminPageHeader from "../../components/admin/AdminPageHeader.vue"

import AdminStatsCard from "../../components/admin/AdminStatsCard.vue"
import AdminQuickAction from "../../components/admin/AdminQuickAction.vue"
import AdminSectionCard from "../../components/admin/AdminSectionCard.vue"
import AdminProgressCard from "../../components/admin/AdminProgressCard.vue"

import AdminBarChart from "../../components/admin/AdminBarChart.vue"
import AdminPieChart from "../../components/admin/AdminPieChart.vue"

import AdminLoading from "../../components/admin/AdminLoading.vue"

import { getDashboard } from "../../services/admin"

const loading = ref(true)

const dashboard = ref({

    total_students: 0,
    active_students: 0,
    blocked_students: 0,

    total_companies: 0,
    approved_companies: 0,
    pending_companies: 0,
    blacklisted_companies: 0,

    total_drives: 0,
    approved_drives: 0,
    pending_drives: 0,
    rejected_drives: 0,
    closed_drives: 0,

    total_applications: 0,

    applied: 0,
    shortlisted: 0,
    selected: 0,
    rejected: 0,

    placement_percentage: 0

})

const today = computed(() => {

    return new Date().toLocaleDateString(

        "en-IN",

        {

            weekday: "long",

            day: "numeric",

            month: "long",

            year: "numeric"

        }

    )

})

const approvalPercentage = computed(() => {

    if (dashboard.value.total_companies === 0)

        return 0

    return Math.round(

        (

            dashboard.value.approved_companies

            /

            dashboard.value.total_companies

        ) * 100

    )

})

const activeStudentPercentage = computed(() => {

    if (dashboard.value.total_students === 0)

        return 0

    return Math.round(

        (

            dashboard.value.active_students

            /

            dashboard.value.total_students

        ) * 100

    )

})

const driveApprovalPercentage = computed(() => {

    if (dashboard.value.total_drives === 0)

        return 0

    return Math.round(

        (

            dashboard.value.approved_drives

            /

            dashboard.value.total_drives

        ) * 100

    )

})

const placementData = computed(() => [

    dashboard.value.applied,

    dashboard.value.shortlisted,

    dashboard.value.selected,

    dashboard.value.rejected

])

const placementLabels = [

    "Applied",

    "Shortlisted",

    "Selected",

    "Rejected"

]

const branchLabels = [

    "Students",

    "Companies",

    "Drives",

    "Applications"

]

const branchValues = computed(() => [

    dashboard.value.total_students,

    dashboard.value.total_companies,

    dashboard.value.total_drives,

    dashboard.value.total_applications

])

const recentActivities = computed(() => [

    {

        icon: "bi bi-buildings",

        color: "success",

        title: `${dashboard.value.pending_companies} Companies Waiting For Approval`

    },

    {

        icon: "bi bi-person-check",

        color: "primary",

        title: `${dashboard.value.active_students} Active Students`

    },

    {

        icon: "bi bi-briefcase",

        color: "warning",

        title: `${dashboard.value.pending_drives} Drives Pending Approval`

    },

    {

        icon: "bi bi-trophy",

        color: "danger",

        title: `${dashboard.value.selected} Students Selected`

    }

])

async function loadDashboard() {

    loading.value = true

    try {

        const response = await getDashboard()


        dashboard.value = {

            total_students: response.students,

            active_students: response.active_students,

            blocked_students: response.blocked_students,


            total_companies: response.companies,

            approved_companies: response.approved_companies,

            pending_companies: response.pending_companies,

            blacklisted_companies: response.blacklisted_companies || 0,


            total_drives: response.placement_drives,

            approved_drives: response.approved_drives,

            pending_drives: response.pending_drives,

            rejected_drives: response.rejected_drives,

            closed_drives: response.closed_drives,


            total_applications: response.applications,


            applied: response.applied,

            shortlisted: response.shortlisted,

            selected: response.selected,

            rejected: response.rejected,


            placement_percentage:

                response.students > 0

                ? Math.round(
                    (response.selected / response.students) * 100
                  )

                : 0

        }


    }

    catch(error){

        console.error(error)

        alert("Unable to load dashboard")

    }

    finally{

        loading.value=false

    }

}
onMounted(() => {

    loadDashboard()

})

</script>


<template>

<div class="admin-layout">

    <AdminSidebar/>

    <div class="admin-content">

        <AdminNavbar/>

        <main class="admin-page">

            <AdminPageHeader

                title="Admin Dashboard"

                subtitle="Placement Portal Overview"

            />

            <AdminLoading
                v-if="loading"
            />

            <template v-else>

                <!-- ================================= -->
                <!-- Welcome Banner -->
                <!-- ================================= -->

                <div class="dashboard-banner mb-5">

                    <div>

                        <h2>

                            Welcome Back 👋

                        </h2>

                        <p>

                            Monitor students, companies, placement drives and analytics from one place.

                        </p>

                    </div>

                    <div class="text-end">

                        <h6 class="mb-2">

                            Today

                        </h6>

                        <h5>

                            {{ today }}

                        </h5>

                    </div>

                </div>

                <!-- ================================= -->
                <!-- Statistics -->
                <!-- ================================= -->

                <div class="row g-4 mb-5">

                    <div class="col-xl-3 col-lg-6">

                        <AdminStatsCard

                            title="Students"

                            :value="dashboard.total_students"

                            subtitle="Registered Students"

                            color="primary"

                            icon="bi bi-mortarboard-fill"

                        />

                    </div>

                    <div class="col-xl-3 col-lg-6">

                        <AdminStatsCard

                            title="Companies"

                            :value="dashboard.total_companies"

                            subtitle="Registered Companies"

                            color="success"

                            icon="bi bi-buildings-fill"

                        />

                    </div>

                    <div class="col-xl-3 col-lg-6">

                        <AdminStatsCard

                            title="Placement Drives"

                            :value="dashboard.total_drives"

                            subtitle="Active Drives"

                            color="warning"

                            icon="bi bi-briefcase-fill"

                        />

                    </div>

                    <div class="col-xl-3 col-lg-6">

                        <AdminStatsCard

                            title="Applications"

                            :value="dashboard.total_applications"

                            subtitle="Applications"

                            color="danger"

                            icon="bi bi-file-earmark-text-fill"

                        />

                    </div>

                </div>

                <!-- ================================= -->
                <!-- Quick Actions -->
                <!-- ================================= -->

                <div class="row g-4 mb-5">

                    <div class="col-xl-3 col-md-6">

                        <AdminQuickAction

                            title="Companies"

                            subtitle="Approve Companies"

                            icon="bi bi-buildings-fill"

                            route="/admin/companies"

                        />

                    </div>

                    <div class="col-xl-3 col-md-6">

                        <AdminQuickAction

                            title="Students"

                            subtitle="Manage Students"

                            icon="bi bi-people-fill"

                            route="/admin/students"

                        />

                    </div>

                    <div class="col-xl-3 col-md-6">

                        <AdminQuickAction

                            title="Placement Drives"

                            subtitle="Manage Drives"

                            icon="bi bi-briefcase-fill"

                            route="/admin/drives"

                        />

                    </div>

                    <div class="col-xl-3 col-md-6">

                        <AdminQuickAction

                            title="Analytics"

                            subtitle="View Reports"

                            icon="bi bi-bar-chart-fill"

                            route="/admin/statistics"

                        />

                    </div>

                </div>

                <!-- ================================= -->
                <!-- Summary Cards -->
                <!-- ================================= -->

                <div class="row g-4 mb-5">

                    <!-- Company Summary -->

                    <div class="col-lg-4">

                        <AdminSectionCard

                            title="Company Summary"

                            icon="bi bi-buildings-fill"

                        >

                            <div class="summary-row">

                                <span>

                                    Approved

                                </span>

                                <strong class="text-success">

                                    {{ dashboard.approved_companies }}

                                </strong>

                            </div>

                            <div class="summary-row">

                                <span>

                                    Pending

                                </span>

                                <strong class="text-warning">

                                    {{ dashboard.pending_companies }}

                                </strong>

                            </div>

                            <div class="summary-row">

                                <span>

                                    Blacklisted

                                </span>

                                <strong class="text-danger">

                                    {{ dashboard.blacklisted_companies }}

                                </strong>

                            </div>

                            <div class="mt-4">

                                <AdminProgressCard

                                    title="Approval Rate"

                                    label="Approved Companies"

                                    :value="dashboard.approved_companies"

                                    :total="dashboard.total_companies"

                                    color="success"

                                    />

                            </div>

                        </AdminSectionCard>

                    </div>

                    <!-- Student Summary -->

                    <div class="col-lg-4">

                        <AdminSectionCard

                            title="Student Summary"

                            icon="bi bi-people-fill"

                        >

                            <div class="summary-row">

                                <span>

                                    Active

                                </span>

                                <strong class="text-success">

                                    {{ dashboard.active_students }}

                                </strong>

                            </div>

                            <div class="summary-row">

                                <span>

                                    Blocked

                                </span>

                                <strong class="text-danger">

                                    {{ dashboard.blocked_students }}

                                </strong>

                            </div>

                            <div class="summary-row">

                                <span>

                                    Active %

                                </span>

                                <strong class="text-primary">

                                    {{ activeStudentPercentage }}%

                                </strong>

                            </div>

                            <div class="mt-4">

                                <AdminProgressCard

                                    title="Student Activity"

                                    label="Active Students"

                                    :value="dashboard.active_students"

                                    :total="dashboard.total_students"

                                    color="primary"

                                />

                            </div>

                        </AdminSectionCard>

                    </div>

                    <!-- Drive Summary -->

                    <div class="col-lg-4">

                        <AdminSectionCard

                            title="Placement Drives"

                            icon="bi bi-briefcase-fill"

                        >

                            <div class="summary-row">

                                <span>

                                    Approved

                                </span>

                                <strong class="text-success">

                                    {{ dashboard.approved_drives }}

                                </strong>

                            </div>

                            <div class="summary-row">

                                <span>

                                    Pending

                                </span>

                                <strong class="text-warning">

                                    {{ dashboard.pending_drives }}

                                </strong>

                            </div>

                            <div class="summary-row">

                                <span>

                                    Closed

                                </span>

                                <strong class="text-secondary">

                                    {{ dashboard.closed_drives }}

                                </strong>

                            </div>

                            <div class="summary-row">

                                <span>

                                    Rejected

                                </span>

                                <strong class="text-danger">

                                    {{ dashboard.rejected_drives }}

                                </strong>

                            </div>

                            <div class="mt-4">

                                <AdminProgressCard

                                    title="Drive Approval"

                                    label="Approved Drives"

                                    :value="dashboard.approved_drives"

                                    :total="dashboard.total_drives"

                                    color="warning"

                                />

                            </div>

                        </AdminSectionCard>

                    </div>

                </div>

                <!-- ================================= -->
                <!-- Placement Results -->
                <!-- ================================= -->

                <div class="row g-4 mb-5">

                    <div class="col-12">

                        <AdminSectionCard

                            title="Placement Results"

                            icon="bi bi-award-fill"

                        >

                            <div class="row text-center">

                                <div class="col-lg-3 col-md-6 mb-3">

                                    <div class="result-box applied">

                                        <i class="bi bi-file-earmark-text-fill"></i>

                                        <h2>

                                            {{ dashboard.applied }}

                                        </h2>

                                        <span>

                                            Applied

                                        </span>

                                    </div>

                                </div>

                                <div class="col-lg-3 col-md-6 mb-3">

                                    <div class="result-box shortlisted">

                                        <i class="bi bi-list-check"></i>

                                        <h2>

                                            {{ dashboard.shortlisted }}

                                        </h2>

                                        <span>

                                            Shortlisted

                                        </span>

                                    </div>

                                </div>

                                <div class="col-lg-3 col-md-6 mb-3">

                                    <div class="result-box selected">

                                        <i class="bi bi-check-circle-fill"></i>

                                        <h2>

                                            {{ dashboard.selected }}

                                        </h2>

                                        <span>

                                            Selected

                                        </span>

                                    </div>

                                </div>

                                <div class="col-lg-3 col-md-6 mb-3">

                                    <div class="result-box rejected">

                                        <i class="bi bi-x-circle-fill"></i>

                                        <h2>

                                            {{ dashboard.rejected }}

                                        </h2>

                                        <span>

                                            Rejected

                                        </span>

                                    </div>

                                </div>

                            </div>

                        </AdminSectionCard>

                    </div>

                </div>

                <!-- ================================= -->
                <!-- Charts -->
                <!-- ================================= -->

                <div class="row g-4 mb-5">

                    <div class="col-xl-8">

                        <AdminBarChart

                            title="Placement Statistics"

                            :labels="placementLabels"

                            :values="placementData"

                        />

                    </div>

                    <div class="col-xl-4">

                        <AdminPieChart

                            title="Placement Distribution"

                            :labels="placementLabels"

                            :values="placementData"

                        />

                    </div>

                </div>

                <!-- ================================= -->
                <!-- Overall Portal Overview -->
                <!-- ================================= -->

                <div class="row g-4 mb-5">

                    <div class="col-xl-7">

                        <AdminSectionCard

                            title="Portal Overview"

                            icon="bi bi-bar-chart-line-fill"

                        >

                            <AdminBarChart

                                :labels="branchLabels"

                                :values="branchValues"

                            />

                        </AdminSectionCard>

                    </div>

                    <div class="col-xl-5">

                        <AdminSectionCard

                            title="Recent Activity"

                            icon="bi bi-clock-history"

                        >

                            <div

                                v-for="(activity,index) in recentActivities"

                                :key="index"

                                class="activity-item"

                            >

                                <div

                                    class="activity-icon"

                                    :class="'bg-'+activity.color"

                                >

                                    <i

                                        :class="activity.icon"

                                    ></i>

                                </div>

                                <div class="activity-content">

                                    <h6>

                                        {{ activity.title }}

                                    </h6>

                                    <small>

                                        Updated from live database

                                    </small>

                                </div>

                            </div>

                        </AdminSectionCard>

                    </div>

                </div>

                <!-- ================================= -->
                <!-- Overall Placement Percentage -->
                <!-- ================================= -->

                <div class="row">

                    <div class="col-12">

                        <AdminSectionCard

                            title="Overall Placement Percentage"

                            icon="bi bi-graph-up-arrow"

                        >

                            <div class="placement-card">

                                <div class="placement-circle">

                                    <h1>

                                        {{ dashboard.placement_percentage || 0 }}%

                                    </h1>

                                </div>

                                <h4 class="mt-4">

                                    Placement Success Rate

                                </h4>

                                <p class="text-muted">

                                    Percentage of students successfully placed
                                    through the Placement Portal.

                                </p>

                            </div>

                        </AdminSectionCard>

                    </div>

                </div>

            </template>

        </main>

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

    display:flex;

    flex-direction:column;

}

.admin-page{

    padding:30px;

}

/* ==================================== */

.dashboard-banner{

    display:flex;

    justify-content:space-between;

    align-items:center;

    background:linear-gradient(

        135deg,

        #4f46e5,

        #6366f1

    );

    color:white;

    border-radius:18px;

    padding:35px;

    margin-bottom:30px;

    box-shadow:0 15px 35px rgba(79,70,229,.25);

}

.dashboard-banner h2{

    font-size:34px;

    font-weight:700;

    margin-bottom:10px;

}

.dashboard-banner p{

    opacity:.9;

    margin:0;

}

/* ==================================== */

.summary-row{

    display:flex;

    justify-content:space-between;

    align-items:center;

    padding:12px 0;

    border-bottom:1px solid #eef2f7;

}

.summary-row:last-child{

    border-bottom:none;

}

/* ==================================== */

.result-box{

    border-radius:16px;

    padding:25px;

    color:white;

    transition:.25s;

}

.result-box:hover{

    transform:translateY(-6px);

    box-shadow:0 15px 30px rgba(0,0,0,.15);

}

.result-box i{

    font-size:28px;

    margin-bottom:15px;

}

.result-box h2{

    font-size:34px;

    font-weight:700;

}

.result-box span{

    font-size:15px;

}

.applied{

    background:#3b82f6;

}

.shortlisted{

    background:#f59e0b;

}

.selected{

    background:#10b981;

}

.rejected{

    background:#ef4444;

}

/* ==================================== */

.activity-item{

    display:flex;

    align-items:center;

    margin-bottom:20px;

}

.activity-item:last-child{

    margin-bottom:0;

}

.activity-icon{

    width:48px;

    height:48px;

    border-radius:50%;

    display:flex;

    justify-content:center;

    align-items:center;

    color:white;

    margin-right:15px;

    flex-shrink:0;

}

.activity-content h6{

    margin:0;

    font-weight:600;

}

.activity-content small{

    color:#6b7280;

}

/* ==================================== */

.placement-card{

    text-align:center;

    padding:35px;

}

.placement-circle{

    width:190px;

    height:190px;

    margin:auto;

    border-radius:50%;

    display:flex;

    justify-content:center;

    align-items:center;

    background:linear-gradient(

        135deg,

        #10b981,

        #34d399

    );

    color:white;

    box-shadow:0 15px 35px rgba(16,185,129,.35);

}

.placement-circle h1{

    font-size:52px;

    font-weight:700;

    margin:0;

}

/* ==================================== */

@media(max-width:992px){

    .dashboard-banner{

        flex-direction:column;

        text-align:center;

        gap:20px;

    }

}

@media(max-width:768px){

    .admin-page{

        padding:18px;

    }

    .placement-circle{

        width:150px;

        height:150px;

    }

    .placement-circle h1{

        font-size:42px;

    }

}

</style>