<script setup>

import { ref } from "vue"

import StudentSidebar from "../../components/student/StudentSidebar.vue"
import StudentNavbar from "../../components/student/StudentNavbar.vue"
import StudentPageHeader from "../../components/student/StudentPageHeader.vue"
import StudentSectionCard from "../../components/student/StudentSectionCard.vue"


import { exportApplications } from "../../services/student"

const exporting = ref(false)

async function exportMyApplications(){

    exporting.value = true

    try{

        const response = await exportApplications()

        alert(response.message)

    }

    catch(error){

        console.error(error)

        alert("Unable to start export")

    }

    finally{

        exporting.value = false

    }

}

</script>

<template>

<div class="student-layout">

    <StudentSidebar />

    <div class="student-content">

        <StudentNavbar />

        <div class="container-fluid mt-4">

            <StudentPageHeader

                title="Export Applications"

                subtitle="Download your placement application history"

            />

            <div class="row justify-content-center">

                <div class="col-lg-8">

                    <StudentSectionCard
                        title="Export CSV"
                    >

                        <p class="text-muted mb-4">

                            Click the button below to generate a CSV containing all of your placement applications.

                            The export runs in the background using Celery.

                            You'll receive a notification when it is ready.

                        </p>

                        <button

                            class="btn btn-primary"

                            @click="exportApplications"

                            :disabled="exporting"

                        >

                            <i class="bi bi-download me-2"></i>

                            {{ exporting ? "Starting Export..." : "Export Applications" }}

                        </button>

                    </StudentSectionCard>

                </div>

            </div>

        </div>

    </div>

</div>

</template>

<style scoped>

.student-layout{

    display:flex;

    min-height:100vh;

    background:#f8fafc;

}

.student-content{

    flex:1;

}

.container-fluid{

    padding:28px;

}

.btn{

    min-width:220px;

    height:46px;

    font-weight:600;

}

</style>