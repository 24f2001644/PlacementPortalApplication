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
import AdminBadge from "../../components/admin/AdminBadge.vue"
import AdminButton from "../../components/admin/AdminButton.vue"
import AdminLoading from "../../components/admin/AdminLoading.vue"
import AdminEmptyState from "../../components/admin/AdminEmptyState.vue"

import {

    getStudents,

    toggleStudentStatus

} from "../../services/admin"

const router = useRouter()

const loading = ref(true)

const search = ref("")

const students = ref([])

/* =========================================
   Statistics
========================================= */

const stats = computed(() => ({

    total: students.value.length,

    active: students.value.filter(

        s => !s.blocked

    ).length,

    blocked: students.value.filter(

        s => s.blocked

    ).length,

    placed: students.value.filter(

        s => s.placement_status === "Selected"

    ).length

}))

/* =========================================
   Search Filter
========================================= */

const filteredStudents = computed(() => {

    if (!search.value)

        return students.value

    const keyword = search.value.toLowerCase()

    return students.value.filter(student =>

        student.name

            .toLowerCase()

            .includes(keyword)

        ||

        student.roll_number

            .toLowerCase()

            .includes(keyword)

        ||

        student.branch

            .toLowerCase()

            .includes(keyword)

    )

})

/* =========================================
   Load Students
========================================= */

async function loadStudents() {

    loading.value = true

    try {

        students.value = await getStudents(

            search.value

        )

    }

    catch (error) {

        console.error(error)

        alert("Unable to load students")

    }

    finally {

        loading.value = false

    }

}

/* =========================================
   Block / Unblock Student
========================================= */

async function toggleStatus(student) {

    try {

        await toggleStudentStatus(

            student.user_id

        )

        await loadStudents()

    }

    catch (error) {

        console.error(error)

        alert("Unable to update student status")

    }

}

/* =========================================
   View Details
========================================= */

function viewStudent(student) {

    router.push(

        `/admin/student/${student.user_id}`

    )

}

/* =========================================
   Badge Color
========================================= */

function badgeColor(student) {

    if (student.blocked)

        return "danger"

    return "success"

}

/* =========================================
   Page Load
========================================= */

onMounted(() => {

    loadStudents()

})

</script>

<template>

<div class="d-flex admin-layout">

    <AdminSidebar />

    <div class="flex-grow-1">

        <AdminNavbar />

        <div class="container-fluid p-4">

            <AdminPageHeader

                title="Students"

                subtitle="Manage Registered Students"

            />

            <!-- ================================= -->
            <!-- Statistics -->
            <!-- ================================= -->

            <div class="row g-4 mb-4">

                <div class="col-xl-3 col-md-6">

                    <AdminStatsCard

                        title="Students"

                        :value="stats.total"

                        subtitle="Registered"

                        color="primary"

                        icon="bi bi-people-fill"

                    />

                </div>

                <div class="col-xl-3 col-md-6">

                    <AdminStatsCard

                        title="Active"

                        :value="stats.active"

                        subtitle="Eligible"

                        color="success"

                        icon="bi bi-person-check-fill"

                    />

                </div>

                <div class="col-xl-3 col-md-6">

                    <AdminStatsCard

                        title="Blocked"

                        :value="stats.blocked"

                        subtitle="Restricted"

                        color="danger"

                        icon="bi bi-person-x-fill"

                    />

                </div>

                <div class="col-xl-3 col-md-6">

                    <AdminStatsCard

                        title="Placed"

                        :value="stats.placed"

                        subtitle="Selected"

                        color="warning"

                        icon="bi bi-award-fill"

                    />

                </div>

            </div>




            <!-- ================================= -->
            <!-- Search -->
            <!-- ================================= -->

            <AdminSectionCard

                title="Search Students"

                icon="bi bi-search"

                class="mb-4"

            >

                <div class="row align-items-center">

                    <div class="col-lg-8">

                        <AdminSearchBar

                            v-model="search"

                            placeholder="Search by Name, Roll Number or Branch..."

                            @input="loadStudents"

                        />

                    </div>

                    <div class="col-lg-4 text-end mt-3 mt-lg-0">

                        <span class="text-muted">

                            Showing

                            <strong>

                                {{ filteredStudents.length }}

                            </strong>

                            students

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
            <!-- Empty State -->
            <!-- ================================= -->

            <AdminEmptyState

                v-else-if="filteredStudents.length===0"

                title="No Students Found"

                description="There are no students matching your search."

                icon="bi bi-people"

            />

            <!-- ================================= -->
            <!-- Students Table -->
            <!-- ================================= -->

            <AdminTableCard

                v-else

                title="Registered Students"

            >

                <div class="table-responsive">

                    <table class="table align-middle table-hover">

                        <thead>

                            <tr>

                                <th>Name</th>

                                <th>Roll Number</th>

                                <th>Branch</th>

                                <th>CGPA</th>

                                <th>Status</th>

                                <th class="text-center">

                                    Actions

                                </th>

                            </tr>

                        </thead>

                        <tbody>

                            <tr

                                v-for="student in filteredStudents"

                                :key="student.user_id"

                            >

                                <td>

                                    <div>

                                        <strong>

                                            {{ student.name }}

                                        </strong>

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

                                        :label="

                                            student.blocked

                                            ? 'Blocked'

                                            : 'Active'

                                        "

                                        :type="badgeColor(student)"

                                    />

                                </td>

                                <td>

                                    <div

                                        class="d-flex justify-content-center gap-2 flex-wrap"

                                    >


                                        <AdminButton

                                            color="primary"

                                            icon="bi bi-eye-fill"

                                            text="View"

                                            @click="viewStudent(student)"

                                        />

                                        <AdminButton

                                            :color="student.blocked ? 'success' : 'danger'"

                                            :icon="student.blocked ? 'bi bi-person-check-fill' : 'bi bi-person-x-fill'"

                                            :text="student.blocked ? 'Unblock' : 'Block'"

                                            @click="toggleStatus(student)"

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

    color:#475569;

    background:#f8fafc;

    border-bottom:2px solid #e2e8f0;

    white-space:nowrap;

}

.table tbody td{

    vertical-align:middle;

    padding:18px 14px;

}

.table tbody tr{

    transition:.25s ease;

}

.table tbody tr:hover{

    background:#f8fbff;

    transform:translateY(-2px);

}

.table strong{

    color:#1e293b;

}

.table-responsive{

    overflow-x:auto;

}

@media(max-width:992px){

    .table td,

    .table th{

        white-space:nowrap;

    }

}

</style>




