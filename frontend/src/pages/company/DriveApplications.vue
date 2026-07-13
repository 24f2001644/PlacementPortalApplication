<script setup>

import { ref, onMounted } from "vue"


import CompanySidebar from "../../components/company/CompanySidebar.vue"
import CompanyNavbar from "../../components/company/CompanyNavbar.vue"
import CompanyPageHeader from "../../components/company/CompanyPageHeader.vue"

import CompanyTableCard from "../../components/company/CompanyTableCard.vue"
import CompanyStatusBadge from "../../components/company/CompanyStatusBadge.vue"
import CompanyLoading from "../../components/company/CompanyLoading.vue"
import CompanyEmptyState from "../../components/company/CompanyEmptyState.vue"



import {

    getApplications,

    updateApplicationStatus

} from "../../services/company"





const applications = ref([])


const loading = ref(true)






async function loadApplications(){


    loading.value=true



    try{


        applications.value = await getApplications()



    }


    catch(error){


        console.error(error)



        alert(

            "Unable to load applications"

        )


    }


    finally{


        loading.value=false


    }


}







async function changeStatus(

    applicationId,

    status

){



    try{



        await updateApplicationStatus(

            applicationId,

            status

        )



        alert(

            "Application status updated"

        )



        loadApplications()



    }



    catch(error){


        console.error(error)



        alert(

            "Unable to update status"

        )


    }


}






onMounted(

    loadApplications

)



</script>


<template>

<div class="company-layout">


    <CompanySidebar />


    <div class="company-content">


        <CompanyNavbar />



        <div class="container-fluid mt-4">



            <CompanyPageHeader

                title="Drive Applications"

                subtitle="Review and manage student applications"

            />





            <CompanyLoading

                v-if="loading"

            />





            <CompanyTableCard

                v-else

                title="Student Applications"

            >





                <table

                    v-if="applications.length"

                    class="table table-hover"

                >




                    <thead>


                        <tr>


                            <th>

                                Student

                            </th>


                            <th>

                                Branch

                            </th>


                            <th>

                                CGPA

                            </th>


                            <th>

                                Skills

                            </th>


                            <th>

                                Resume

                            </th>


                            <th>

                                Status

                            </th>


                            <th>

                                Action

                            </th>


                        </tr>


                    </thead>







                    <tbody>




                        <tr

                            v-for="application in applications"

                            :key="application.application_id"

                        >




                            <td>


                                <strong>

                                    {{ application.student }}

                                </strong>


                                <br>


                                <small class="text-muted">

                                    {{ application.roll_number }}

                                </small>


                            </td>





                            <td>


                                {{ application.branch }}


                            </td>





                            <td>


                                {{ application.cgpa }}


                            </td>





                            <td>


                                {{ application.skills }}


                            </td>





                            <td>


                                <a

                                    :href="application.resume"

                                    target="_blank"

                                    class="btn btn-outline-primary btn-sm"

                                >


                                    <i class="bi bi-file-earmark-pdf"></i>


                                    View


                                </a>


                            </td>







                            <td>



                                <CompanyStatusBadge

                                    :status="application.status"

                                />



                            </td>







                            <td>



                                <div class="action-buttons">





                                    <button

                                        class="btn btn-success btn-sm"

                                        @click="changeStatus(application.application_id,'Shortlisted')"

                                        v-if="application.status==='Applied'"

                                    >


                                        Shortlist


                                    </button>







                                    <button

                                        class="btn btn-danger btn-sm"

                                        @click="changeStatus(application.application_id,'Rejected')"

                                        v-if="application.status==='Applied'"

                                    >


                                        Reject


                                    </button>







                                    <button

                                        class="btn btn-primary btn-sm"

                                        @click="changeStatus(application.application_id,'Selected')"

                                        v-if="application.status==='Shortlisted'"

                                    >


                                        Select


                                    </button>





                                </div>



                            </td>






                        </tr>





                    </tbody>






                </table>






                <CompanyEmptyState


                    v-else


                    icon="bi bi-people"


                    title="No Applications"


                    message="Students who apply for your drives will appear here."

                />





            </CompanyTableCard>





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



.table{

    margin-bottom:0;

}



.table th{

    color:#475569;

    font-weight:600;

    white-space:nowrap;

}



.table td{

    vertical-align:middle;

    color:#334155;

}



.text-muted{

    font-size:13px;

}



.action-buttons{

    display:flex;

    gap:8px;

    flex-wrap:wrap;

}



.btn{

    border-radius:8px;

    font-weight:500;

}



.btn-success{

    background:#16A34A;

    border:none;

}



.btn-success:hover{

    background:#15803D;

}



.btn-danger{

    background:#DC2626;

    border:none;

}



.btn-danger:hover{

    background:#B91C1C;

}



.btn-primary{

    background:#2563EB;

    border:none;

}



.btn-primary:hover{

    background:#1D4ED8;

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



    .action-buttons{

        flex-direction:column;

    }

}

</style>