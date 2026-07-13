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

} from "../../services/admin"

const loading = ref(false)

const search = ref("")

const status = ref("")

const applications = ref([])

const statusOptions = [

    "Applied",

    "Shortlisted",

    "Selected",

    "Rejected"

]

async function loadApplications(){

    loading.value = true

    try{

        applications.value = await getApplications(

    search.value,

    status.value

)

    }

    catch(err){

        console.error(err)

        alert("Unable to load applications")

    }

    finally{

        loading.value = false

    }

}

const filteredApplications = computed(()=>{

    return applications.value.filter(app=>{

        if(status.value==="") return true

        return app.status===status.value

    })

})

async function approve(app){

    try{

        await updateApplicationStatus(

            app.application_id,

            "Selected"

        )

        await loadApplications()

    }

    catch(err){

        console.error(err)

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

    catch(err){

        console.error(err)

        alert("Unable to update application")

    }

}

onMounted(loadApplications)

</script>

<template>

<div class="d-flex admin-layout">

    <AdminSidebar/>

    <div class="flex-grow-1">

        <AdminNavbar/>

        <div class="container-fluid p-4">

            <AdminPageHeader

                title="Applications"

                subtitle="Manage placement applications"

            />

            <AdminTableCard>

                <div class="row mb-4">

                    <div class="col-lg-6">

                        <AdminSearchBar

                            v-model="search"

                            placeholder="Search Student"

                            @keyup.enter="loadApplications"

                        />

                    </div>

                    <div class="col-lg-3">

                        <AdminFilterBar

                            v-model="status"

                            label="Status"

                            :options="statusOptions"

                        />

                    </div>

                    <div class="col-lg-3 text-end">

                        <button

                            class="btn btn-primary"

                            @click="loadApplications"

                        >

                            Search

                        </button>

                    </div>

                </div>

                <AdminLoading

                    v-if="loading"

                />

                <AdminEmptyState

                    v-else-if="filteredApplications.length===0"

                    title="No Applications Found"

                    message="No application matches your filters."

                />

                <table

                    v-else

                    class="table table-hover align-middle"

                >

                    <thead>

                        <tr>

                            <th>Student</th>

                            <th>Company</th>

                            <th>Role</th>

                            <th>Status</th>

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

                                    {{ app.student_name }}

                                </strong>

                            </td>

                            <td>

                                {{ app.company }}

                            </td>

                            <td>

                                {{ app.job_title }}

                            </td>

                            <td>

                                <AdminBadge

                                    :status="app.status"

                                />

                            </td>

                            <td>

                                <div

                                    class="d-flex gap-2 justify-content-center"

                                >

                                    <AdminButton

                                        text="Approve"

                                        color="success"

                                        icon="bi bi-check-circle"

                                        @click="approve(app)"

                                    />

                                    <AdminButton

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