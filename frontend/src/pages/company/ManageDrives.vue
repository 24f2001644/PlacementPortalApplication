<script setup>

import { ref, onMounted } from "vue"


import CompanySidebar from "../../components/company/CompanySidebar.vue"
import CompanyNavbar from "../../components/company/CompanyNavbar.vue"
import CompanyPageHeader from "../../components/company/CompanyPageHeader.vue"
import CompanyTableCard from "../../components/company/CompanyTableCard.vue"
import CompanyStatusBadge from "../../components/company/CompanyStatusBadge.vue"
import CompanyEmptyState from "../../components/company/CompanyEmptyState.vue"
import CompanyLoading from "../../components/company/CompanyLoading.vue"


import {

    getDrives,
    closeDrive

} from "../../services/company"





const drives = ref([])


const loading = ref(true)



async function loadDrives(){


    loading.value=true



    try{


        drives.value = await getDrives()



    }


    catch(error){


        console.error(error)


        alert(

            "Unable to load drives"

        )


    }


    finally{


        loading.value=false


    }


}





async function closePlacementDrive(id){


    if(

        !confirm(

            "Are you sure you want to close this drive?"

        )

    )

        return




    try{


        await closeDrive(id)



        alert(

            "Drive closed successfully"

        )



        loadDrives()



    }


    catch(error){


        console.error(error)


        alert(

            "Unable to close drive"

        )


    }


}




onMounted(

    loadDrives

)



</script>

<template>

<div class="company-layout">


    <CompanySidebar />



    <div class="company-content">



        <CompanyNavbar />



        <div class="container-fluid mt-4">



            <CompanyPageHeader

                title="Manage Placement Drives"

                subtitle="View and manage your created placement opportunities"

            />





            <CompanyLoading

                v-if="loading"

            />






            <CompanyTableCard

                v-else

                title="Your Drives"

            >





                <table

                    v-if="drives.length"

                    class="table table-hover"

                >



                    <thead>


                        <tr>


                            <th>

                                Role

                            </th>


                            <th>

                                Package

                            </th>


                            <th>

                                Location

                            </th>


                            <th>

                                Deadline

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

                            v-for="drive in drives"

                            :key="drive.id"

                        >



                            <td>


                                {{ drive.role }}


                            </td>





                            <td>


                                {{ drive.package }}


                            </td>





                            <td>


                                {{ drive.location }}


                            </td>





                            <td>


                                {{ drive.deadline }}


                            </td>







                            <td>



                                <CompanyStatusBadge

                                    :status="drive.status"

                                />



                            </td>






                            <td>



                                <button


                                    v-if="drive.status === 'Approved'"



                                    class="btn btn-danger btn-sm"



                                    @click="closePlacementDrive(drive.id)"


                                >



                                    <i class="bi bi-x-circle me-1"></i>


                                    Close



                                </button>




                                <span

                                    v-else

                                    class="text-muted"

                                >

                                    No Action

                                </span>




                            </td>







                        </tr>




                    </tbody>




                </table>





                <CompanyEmptyState

                    v-else

                    icon="bi bi-briefcase"

                    title="No Drives Created"

                    message="Create your first placement drive to start hiring students."

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



.btn-danger{

    border-radius:8px;

    padding:6px 12px;

    font-size:14px;

}



.text-muted{

    font-size:14px;

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


    .table{

        font-size:14px;

    }

}

</style>