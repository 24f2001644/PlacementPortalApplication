<script setup>

import { ref, onMounted } from "vue"

import AdminSidebar from "../../components/admin/AdminSidebar.vue"
import AdminNavbar from "../../components/admin/AdminNavbar.vue"
import AdminPageHeader from "../../components/admin/AdminPageHeader.vue"
import AdminTableCard from "../../components/admin/AdminTableCard.vue"
import AdminSearchBar from "../../components/admin/AdminSearchBar.vue"
import AdminBadge from "../../components/admin/AdminBadge.vue"
import AdminButton from "../../components/admin/AdminButton.vue"
import AdminLoading from "../../components/admin/AdminLoading.vue"
import AdminEmptyState from "../../components/admin/AdminEmptyState.vue"

import {

    getCompanies,

    approveCompany,

    rejectCompany,

    blacklistCompany

}

from "../../services/admin"

const companies = ref([])

const search = ref("")

const loading = ref(false)

async function loadCompanies(){

    loading.value = true

    try{

        companies.value = await getCompanies(

            search.value

        )

    }

    catch(err){

        console.error(err)

        alert("Unable to load companies")

    }

    finally{

        loading.value = false

    }

}

async function approve(id){

    try{

        await approveCompany(id)

        await loadCompanies()

    }

    catch(err){

        console.error(err)

        alert("Approval Failed")

    }

}

async function reject(id){

    if(!confirm("Reject this company?"))

        return

    try{

        await rejectCompany(id)

        await loadCompanies()

    }

    catch(err){

        console.error(err)

        alert("Reject Failed")

    }

}

async function blacklist(id){

    try{

        await blacklistCompany(id)

        await loadCompanies()

    }

    catch(err){

        console.error(err)

        alert("Operation Failed")

    }

}

onMounted(loadCompanies)

</script>

<template>

<div class="d-flex admin-layout">

    <AdminSidebar/>

    <div class="flex-grow-1">

        <AdminNavbar/>

        <div class="container-fluid p-4">

            <AdminPageHeader

                title="Company Management"

                subtitle="Approve, Reject and Blacklist Companies"

            />

            <AdminTableCard>

                <div class="row mb-4">

                    <div class="col-lg-6">

                        <AdminSearchBar

                            v-model="search"

                            placeholder="Search Company..."

                            @keyup.enter="loadCompanies"

                        />

                    </div>

                    <div class="col-lg-2">

                        <button

                            class="btn btn-primary w-100"

                            @click="loadCompanies"

                        >

                            <i class="bi bi-search me-2"></i>

                            Search

                        </button>

                    </div>

                </div>

                <AdminLoading

                    v-if="loading"

                />

                <AdminEmptyState

                    v-else-if="companies.length===0"

                    title="No Companies Found"

                    message="No registered companies available."

                />

                <table

                    v-else

                    class="table table-hover align-middle"

                >

                    <thead>

                        <tr>

                            <th>Company</th>

                            <th>Industry</th>

                            <th>Location</th>

                            <th>HR</th>

                            <th>Email</th>

                            <th>Status</th>

                            <th>Blacklist</th>

                            <th class="text-center">

                                Actions

                            </th>

                        </tr>

                    </thead>

                    <tbody>

                        <tr

                            v-for="company in companies"

                            :key="company.user_id"

                        >

                            <td>

                                <strong>

                                    {{ company.company_name }}

                                </strong>

                            </td>

                            <td>

                                {{ company.industry }}

                            </td>

                            <td>

                                {{ company.location }}

                            </td>

                            <td>

                                {{ company.hr_name }}

                            </td>

                            <td>

                                {{ company.hr_email }}

                            </td>

                            <td>

                                <AdminBadge

                                    :status="company.approved ? 'Approved' : 'Pending'"

                                />

                            </td>

                            <td>

                                <AdminBadge

                                    :status="company.blacklisted ? 'Rejected' : 'Selected'"

                                >

                                </AdminBadge>

                            </td>

                            <td>

                                <div

                                    class="d-flex gap-2 justify-content-center flex-wrap"

                                >

                                    <AdminButton

                                        text="Approve"

                                        icon="bi bi-check-circle"

                                        color="success"

                                        :disabled="company.approved"

                                        @click="approve(company.user_id)"

                                    />

                                    <AdminButton

                                        :text="company.blacklisted ? 'Unblacklist' : 'Blacklist'"

                                        icon="bi bi-slash-circle"

                                        color="warning"

                                        @click="blacklist(company.user_id)"

                                    />

                                    <AdminButton

                                        text="Reject"

                                        icon="bi bi-trash"

                                        color="danger"

                                        @click="reject(company.user_id)"

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