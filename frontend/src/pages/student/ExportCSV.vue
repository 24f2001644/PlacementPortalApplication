<script setup>

import StudentSidebar from "../../components/student/StudentSidebar.vue"
import StudentNavbar from "../../components/student/StudentNavbar.vue"
import StudentPageHeader from "../../components/student/StudentPageHeader.vue"
import StudentSectionCard from "../../components/student/StudentSectionCard.vue"

import {

    exportApplications

} from "../../services/student"



async function exportCSV(){

    try{

        const response = await exportApplications()

        const url = window.URL.createObjectURL(

            new Blob(

                [response.data]

            )

        )

        const link = document.createElement(

            "a"

        )

        link.href = url

        link.download = "applications.csv"

        link.click()

        window.URL.revokeObjectURL(url)

    }

    catch(error){

        console.error(error)

        alert(

            "Unable to export CSV"

        )

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

                subtitle="Download your placement application history as a CSV file"

            />



            <StudentSectionCard

                title="Export Placement Data"

            >

                <div class="text-center py-5">

                    <div class="export-icon">

                        <i class="bi bi-file-earmark-arrow-down-fill"></i>

                    </div>



                    <h4 class="mt-4">

                        Download Your Applications

                    </h4>



                    <p class="text-muted mt-3">

                        Export all your placement applications including company,

                        role, application status, and applied date into a CSV file.

                        You can use it for your records or further analysis.

                    </p>



                    <button

                        class="btn btn-success btn-lg mt-4"

                        @click="exportCSV"

                    >

                        <i class="bi bi-download me-2"></i>

                        Export CSV

                    </button>

                </div>

            </StudentSectionCard>

        </div>

    </div>

</div>

</template>

<style scoped>

.student-layout{

    display:flex;

    min-height:100vh;

    background:#F8FAFC;

}



.student-content{

    flex:1;

}



.container-fluid{

    padding:25px;

}



.export-icon{

    width:120px;

    height:120px;

    margin:auto;

    border-radius:50%;

    background:#DCFCE7;

    display:flex;

    align-items:center;

    justify-content:center;

}



.export-icon i{

    font-size:55px;

    color:#16A34A;

}



h4{

    color:#1E293B;

    font-weight:700;

}



p{

    max-width:650px;

    margin:auto;

    line-height:1.8;

    color:#64748B;

}



.btn{

    border-radius:12px;

    padding:12px 28px;

    font-weight:600;

}



.btn i{

    font-size:16px;

}



@media(max-width:992px){

    .container-fluid{

        padding:20px;

    }

}



@media(max-width:768px){

    .student-layout{

        flex-direction:column;

    }



    .student-content{

        width:100%;

    }



    .container-fluid{

        padding:15px;

    }



    .export-icon{

        width:90px;

        height:90px;

    }



    .export-icon i{

        font-size:42px;

    }



    .btn{

        width:100%;

    }

}

</style>