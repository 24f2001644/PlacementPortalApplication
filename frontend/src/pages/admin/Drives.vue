<script setup>

import { ref, computed, onMounted } from "vue"
import { useRouter } from "vue-router"

import AdminSidebar from "../../components/admin/AdminSidebar.vue"
import AdminNavbar from "../../components/admin/AdminNavbar.vue"
import AdminPageHeader from "../../components/admin/AdminPageHeader.vue"
import AdminStatsCard from "../../components/admin/AdminStatsCard.vue"
import AdminSectionCard from "../../components/admin/AdminSectionCard.vue"
import AdminTableCard from "../../components/admin/AdminTableCard.vue"
import AdminSearchBar from "../../components/admin/AdminSearchBar.vue"
import AdminButton from "../../components/admin/AdminButton.vue"
import AdminBadge from "../../components/admin/AdminBadge.vue"
import AdminLoading from "../../components/admin/AdminLoading.vue"
import AdminEmptyState from "../../components/admin/AdminEmptyState.vue"
import AdminConfirmModal from "../../components/admin/AdminConfirmModal.vue"

import {

    getDrives,
    approveDrive,
    rejectDrive,
    closeDrive

} from "../../services/admin"

const router = useRouter()

const loading = ref(true)

const search = ref("")

const selectedDrive = ref(null)

const drives = ref([])

/* ======================================
   Dashboard Statistics
====================================== */

const stats = computed(() => {

    return {

        total: drives.value.length,

        approved: drives.value.filter(

            d => d.status === "Approved"

        ).length,

        pending: drives.value.filter(

            d => d.status === "Pending"

        ).length,

        rejected: drives.value.filter(

            d => d.status === "Rejected"

        ).length,

        closed: drives.value.filter(

            d => d.status === "Closed"

        ).length

    }

})

/* ======================================
   Search Filter
====================================== */

const filteredDrives = computed(() => {

    if (!search.value)

        return drives.value

    return drives.value.filter(d =>

        d.company

            .toLowerCase()

            .includes(

                search.value.toLowerCase()

            )

        ||

        d.job_title

            .toLowerCase()

            .includes(

                search.value.toLowerCase()

            )

    )

})

/* ======================================
   Load Drives
====================================== */

async function loadDrives() {

    loading.value = true

    try {

        drives.value = await getDrives(

            search.value

        )

    }

    catch (error) {

        console.error(error)

        alert("Unable to load placement drives")

    }

    finally {

        loading.value = false

    }

}

/* ======================================
   Approve
====================================== */

async function approve(id) {

    try {

        await approveDrive(id)

        await loadDrives()

    }

    catch (error) {

        console.error(error)

        alert("Unable to approve drive")

    }

}

/* ======================================
   Close
====================================== */

async function closePlacementDrive(id) {

    try {

        await closeDrive(id)

        await loadDrives()

    }

    catch (error) {

        console.error(error)

        alert("Unable to close drive")

    }

}

/* ======================================
   Reject Drive
====================================== */

function openRejectModal(drive) {

    selectedDrive.value = drive

}

async function confirmReject() {

    if (!selectedDrive.value)

        return

    try {

        await rejectDrive(

            selectedDrive.value.drive_id

        )

        selectedDrive.value = null

        await loadDrives()

    }

    catch (error) {

        console.error(error)

        alert("Unable to reject drive")

    }

}

/* ======================================
   View Details
====================================== */

function openDetails(id) {

    router.push(

        `/admin/drives/${id}`

    )

}

/* ======================================
   Badge Color
====================================== */

function badgeColor(status) {

    switch (status) {

        case "Approved":

            return "success"

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

/* ======================================
   Load Page
====================================== */

onMounted(() => {

    loadDrives()

})

</script>

<template>

<div class="d-flex admin-layout">

    <AdminSidebar />

    <div class="flex-grow-1">

        <AdminNavbar />

        <div class="container-fluid p-4">

            <AdminPageHeader

                title="Placement Drives"

                subtitle="Manage, Approve and Monitor Company Placement Drives"

            />

            <!-- ================================= -->
            <!-- Statistics -->
            <!-- ================================= -->

            <div class="row g-4 mb-4">

                <div class="col-xl-2 col-md-4 col-sm-6">

                    <AdminStatsCard

                        title="Total"

                        :value="stats.total"

                        subtitle="All Drives"

                        color="primary"

                        icon="bi bi-briefcase-fill"

                    />

                </div>

                <div class="col-xl-2 col-md-4 col-sm-6">

                    <AdminStatsCard

                        title="Approved"

                        :value="stats.approved"

                        subtitle="Live"

                        color="success"

                        icon="bi bi-check-circle-fill"

                    />

                </div>

                <div class="col-xl-2 col-md-4 col-sm-6">

                    <AdminStatsCard

                        title="Pending"

                        :value="stats.pending"

                        subtitle="Waiting"

                        color="warning"

                        icon="bi bi-clock-history"

                    />

                </div>

                <div class="col-xl-2 col-md-4 col-sm-6">

                    <AdminStatsCard

                        title="Closed"

                        :value="stats.closed"

                        subtitle="Completed"

                        color="secondary"

                        icon="bi bi-lock-fill"

                    />

                </div>

                <div class="col-xl-2 col-md-4 col-sm-6">

                    <AdminStatsCard

                        title="Rejected"

                        :value="stats.rejected"

                        subtitle="Rejected"

                        color="danger"

                        icon="bi bi-x-circle-fill"

                    />

                </div>

            </div>
            <!-- ================================= -->
            <!-- Search -->
            <!-- ================================= -->

            <AdminSectionCard
                title="Search Placement Drives"
                icon="bi bi-search"
                class="mb-4"
            >

                <div class="row align-items-center">

                    <div class="col-lg-8">

                        <AdminSearchBar

                            v-model="search"

                            placeholder="Search by company or job title..."

                            @input="loadDrives"

                        />

                    </div>

                    <div class="col-lg-4 text-end mt-3 mt-lg-0">

                        <span class="text-muted">

                            Showing

                            <strong>

                                {{ filteredDrives.length }}

                            </strong>

                            drives

                        </span>

                    </div>

                </div>

            </AdminSectionCard>

            <!-- ================================= -->
            <!-- Loading -->
            <!-- ================================= -->

            <AdminLoading

                v-if="loading"

            />

            <!-- ================================= -->
            <!-- Empty -->
            <!-- ================================= -->

            <AdminEmptyState

                v-else-if="filteredDrives.length===0"

                title="No Placement Drives"

                description="No placement drives match your search."

                icon="bi bi-briefcase"

            />

            <!-- ================================= -->
            <!-- Table -->
            <!-- ================================= -->

            <AdminTableCard

                v-else

                title="Placement Drives"

            >

                <div class="table-responsive">

                    <table class="table align-middle table-hover">

                        <thead>

                            <tr>

                                <th>Company</th>

                                <th>Job Title</th>

                                <th>Package</th>

                                <th>Deadline</th>

                                <th>Status</th>

                                <th class="text-center">

                                    Actions

                                </th>

                            </tr>

                        </thead>

                        <tbody>

                            <tr

                                v-for="drive in filteredDrives"

                                :key="drive.drive_id"

                            >

                                <td>

                                    <div>

                                        <strong>

                                            {{ drive.company }}

                                        </strong>

                                    </div>

                                </td>

                                <td>

                                    {{ drive.job_title }}

                                </td>

                                <td>

                                    {{ drive.salary_package }}

                                </td>

                                <td>

                                    {{ drive.application_deadline }}

                                </td>

                                <td>

                                    <AdminBadge

                                        :label="drive.status"

                                        :type="badgeColor(drive.status)"

                                    />

                                </td>

                                <td>

                                    <div

                                        class="d-flex flex-wrap justify-content-center gap-2"

                                    >

                                        <AdminButton

                                            color="success"

                                            icon="bi bi-check-circle-fill"

                                            text="Approve"

                                            :disabled="drive.status==='Approved'"

                                            @click="approve(drive.drive_id)"

                                        />

                                        <AdminButton

                                            color="warning"

                                            icon="bi bi-lock-fill"

                                            text="Close"

                                            :disabled="drive.status==='Closed'"

                                            @click="closePlacementDrive(drive.drive_id)"

                                        />

                                        <AdminButton

                                            color="danger"

                                            icon="bi bi-x-circle-fill"

                                            text="Reject"

                                            @click="openRejectModal(drive)"

                                        />

                                        <AdminButton

                                            color="primary"

                                            icon="bi bi-eye-fill"

                                            text="Details"

                                            @click="openDetails(drive.drive_id)"

                                        />

                                    </div>

                                </td>

                            </tr>

                        </tbody>

                    </table>

                </div>

            </AdminTableCard>

        </div>

    </div>

    <!-- =============================== -->
    <!-- Reject Confirmation Modal -->
    <!-- =============================== -->

    <AdminConfirmModal

        :show="selectedDrive!==null"

        title="Reject Placement Drive"

        message="Are you sure you want to reject this placement drive?"

        confirmText="Reject"

        confirmColor="danger"

        @confirm="confirmReject"

        @cancel="selectedDrive=null"

    />

</div>

</template>

<style scoped>

.admin-layout{

    min-height:100vh;

    background:#f4f7fb;

}

.table{

    margin-bottom:0;

}

.table thead th{

    font-weight:700;

    color:#4b5563;

    border-bottom:2px solid #eef2f7;

    white-space:nowrap;

    background:#fafbff;

}

.table tbody td{

    vertical-align:middle;

    padding:18px 14px;

}

.table tbody tr{

    transition:all .25s ease;

}

.table tbody tr:hover{

    background:#f8faff;

    transform:translateY(-2px);

}

.table strong{

    color:#1e293b;

}

.table-responsive{

    overflow-x:auto;

}

@media (max-width:992px){

    .table td,

    .table th{

        white-space:nowrap;

    }

}

</style>

