<script setup>

import {
    ref,
    onMounted,
    onBeforeUnmount
} from "vue"



import AdminSidebar from "../../components/admin/AdminSidebar.vue"
import AdminNavbar from "../../components/admin/AdminNavbar.vue"
import AdminPageHeader from "../../components/admin/AdminPageHeader.vue"

import AdminSectionCard from "../../components/admin/AdminSectionCard.vue"
import AdminTableCard from "../../components/admin/AdminTableCard.vue"

import AdminLoading from "../../components/admin/AdminLoading.vue"
import AdminEmptyState from "../../components/admin/AdminEmptyState.vue"



import {

    exportCSV,

    getExportStatus,

    downloadCSV

} from "../../services/admin"




/*
==========================================
STATE
==========================================
*/


const loading = ref(true)

const exporting = ref(false)

const exports = ref([])

const refreshTimer = ref(null)




/*
==========================================
LOAD EXPORTS
==========================================
*/


async function loadExports(){

    if(exports.value.length===0){

        loading.value=false
        return

    }

    try{

        const updated=[]

        for(const job of exports.value){

            const status=await getExportStatus(job.export_id)

            updated.push(status)

        }

        exports.value=updated

    }

    catch(error){

        console.error(error)

    }

    finally{

        loading.value=false

    }

}




/*
==========================================
START EXPORT
==========================================
*/


async function startExport(){

    try{

        exporting.value = true

        const response = await exportCSV()

        console.log(response)

        // If backend returns export_id
        if(response.export_id){

            const status = await getExportStatus(

                response.export_id

            )

            exports.value = [status]

        }

    }

    catch(error){

      console.error(error)

      console.log(error.response)

      console.log(error.response?.data)

      alert(error.response?.data?.message || "Unable to start export.")

  }

    finally{

        exporting.value = false

    }

}




/*
==========================================
DOWNLOAD CSV
==========================================
*/


async function download(id){

    try{

        const blob = await downloadCSV(id)

        const url = window.URL.createObjectURL(blob)

        const link = document.createElement("a")

        link.href = url

        link.download = `applications_${id}.csv`

        document.body.appendChild(link)

        link.click()

        link.remove()

        window.URL.revokeObjectURL(url)

    }

    catch(error){

        console.error(error)

        alert("Download failed.")

    }

}




/*
==========================================
STATUS COLOR
==========================================
*/


function badgeClass(status){

    switch(status){

        case "COMPLETED":

            return "bg-success"

        case "PROCESSING":

            return "bg-warning text-dark"

        case "FAILED":

            return "bg-danger"

        default:

            return "bg-secondary"

    }

}




/*
==========================================
DATE FORMAT
==========================================
*/


function formatDate(date){

    if(!date){

        return "-"

    }

    return new Date(date).toLocaleString()

}




/*
==========================================
AUTO REFRESH
==========================================
*/


onMounted(async()=>{

    await loadExports()

    refreshTimer.value = setInterval(

        loadExports,

        3000

    )

})




onBeforeUnmount(()=>{

    clearInterval(

        refreshTimer.value

    )

})

</script>

<template>

<div class="admin-layout">

    <AdminSidebar/>

    <div class="admin-content">

        <AdminNavbar/>

        <div class="container-fluid p-4">

            <AdminPageHeader

                title="Export Applications"

                subtitle="Generate and download placement application reports"

            />



            <AdminLoading

                v-if="loading"

            />



            <template v-else>



                <!-- ACTIONS -->

                <AdminSectionCard

                    title="CSV Export"

                >

                    <div class="d-flex flex-wrap gap-3">

                        <button

                            class="btn btn-success"

                            @click="startExport"

                            :disabled="exporting"

                        >

                            <i class="bi bi-file-earmark-arrow-down me-2"></i>

                            {{ exporting ? "Starting Export..." : "Export Applications CSV" }}

                        </button>



                        <button

                            class="btn btn-outline-primary"

                            @click="loadExports"

                        >

                            <i class="bi bi-arrow-clockwise me-2"></i>

                            Refresh

                        </button>

                    </div>

                </AdminSectionCard>



                <!-- EXPORT TABLE -->

                <AdminTableCard

                    title="Export History"

                >

                    <template

                        v-if="exports.length"

                    >

                        <table class="table table-hover align-middle">

                            <thead>

                                <tr>

                                    <th>Export ID</th>

                                    <th>Status</th>

                                    <th>Created At</th>

                                    <th>Completed At</th>

                                    <th>Action</th>

                                </tr>

                            </thead>



                            <tbody>

                                <tr

                                    v-for="job in exports"

                                    :key="job.export_id"

                                >

                                    <td>

                                        {{ job.export_id }}

                                    </td>



                                    <td>

                                        <span

                                            class="badge rounded-pill"

                                            :class="badgeClass(job.status)"

                                        >

                                            {{ job.status }}

                                        </span>

                                    </td>



                                    <td>

                                        {{ formatDate(job.created_at) }}

                                    </td>



                                    <td>

                                        {{ formatDate(job.completed_at) }}

                                    </td>



                                    <td>

                                        <button

                                            v-if="job.status==='COMPLETED'"

                                            class="btn btn-success btn-sm"

                                            @click="download(job.export_id)"

                                        >

                                            <i class="bi bi-download me-1"></i>

                                            Download

                                        </button>



                                        <span

                                            v-else-if="job.status==='FAILED'"

                                            class="badge bg-danger"

                                        >

                                            Failed

                                        </span>



                                        <span

                                            v-else

                                            class="badge bg-warning text-dark"

                                        >

                                            Processing...

                                        </span>

                                    </td>

                                </tr>

                            </tbody>

                        </table>

                    </template>



                    <AdminEmptyState

                        v-else

                        title="No Export Jobs"

                        description="Generate your first CSV export using the button above."

                    />

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

.badge{
padding:8px 12px;
font-size:13px;
border-radius:20px;
}

.btn{
border-radius:8px;
}

</style>