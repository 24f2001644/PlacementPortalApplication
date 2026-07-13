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

    getSelectedStudents

} from "../../services/company"






const loading = ref(true)



const students = ref([])







async function loadSelectedStudents(){



    loading.value=true




    try{


        students.value = await getSelectedStudents()



    }


    catch(error){



        console.error(error)



        alert(

            "Unable to load selected students"

        )



    }


    finally{


        loading.value=false


    }


}







onMounted(

    loadSelectedStudents

)



</script>

<template>

<div class="company-layout">


    <CompanySidebar />



    <div class="company-content">



        <CompanyNavbar />



        <div class="container-fluid mt-4">





            <CompanyPageHeader

                title="Selected Students"

                subtitle="View final candidates selected for hiring"

            />







            <CompanyLoading

                v-if="loading"

            />









            <CompanyTableCard

                v-else

                title="Selected Candidates"

            >






                <table

                    v-if="students.length"

                    class="table table-hover"

                >



                    <thead>


                        <tr>



                            <th>

                                Student

                            </th>




                            <th>

                                Roll Number

                            </th>




                            <th>

                                Branch

                            </th>




                            <th>

                                CGPA

                            </th>




                            <th>

                                Role

                            </th>




                            <th>

                                Package

                            </th>




                            <th>

                                Selection Date

                            </th>




                            <th>

                                Status

                            </th>



                        </tr>



                    </thead>







                    <tbody>



                        <tr

                            v-for="student in students"

                            :key="student.application_id"

                        >





                            <td>


                                <strong>

                                    {{ student.student }}

                                </strong>


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


                                {{ student.role }}


                            </td>





                            <td>


                                {{ student.package }}


                            </td>





                            <td>


                                {{ student.selection_date }}


                            </td>







                            <td>



                                <CompanyStatusBadge

                                    status="Selected"

                                />



                            </td>






                        </tr>







                    </tbody>







                </table>









                <CompanyEmptyState

                    v-else

                    icon="bi bi-person-check"

                    title="No Selected Students"

                    message="Students selected after interviews will appear here."

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



strong{

    color:#0F172A;

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