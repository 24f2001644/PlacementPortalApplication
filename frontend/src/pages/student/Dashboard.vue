<script setup>


import {ref,onMounted,computed} from "vue"



import StudentSidebar from "../../components/student/StudentSidebar.vue"

import StudentNavbar from "../../components/student/StudentNavbar.vue"

import StudentPageHeader from "../../components/student/StudentPageHeader.vue"

import StudentStatsCard from "../../components/student/StudentStatsCard.vue"

import StudentSectionCard from "../../components/student/StudentSectionCard.vue"

import StudentTableCard from "../../components/student/StudentTableCard.vue"

import StudentProgressCard from "../../components/student/StudentProgressCard.vue"

import StudentLoading from "../../components/student/StudentLoading.vue"

import StudentEmptyState from "../../components/student/StudentEmptyState.vue"



import {

    getStudentDashboard

} from "../../services/student"



const loading=ref(true)



const dashboard=ref({


    name:"",


    total_drives:0,


    applied_drives:0,


    shortlisted:0,


    selected:0,


    profile_completion:0,


    recent_applications:[]


})





const cards=computed(()=>[


{

title:"Available Drives",

value:dashboard.value.total_drives,

icon:"bi bi-briefcase-fill"

},



{

title:"Applied",

value:dashboard.value.applied_drives,

icon:"bi bi-file-earmark-text"

},



{

title:"Shortlisted",

value:dashboard.value.shortlisted,

icon:"bi bi-person-check"

},



{

title:"Selected",

value:dashboard.value.selected,

icon:"bi bi-award-fill"

}



])




async function loadDashboard(){


    try{


        dashboard.value=await getStudentDashboard()


    }


    catch(error){


        console.error(error)

        alert("Unable to load dashboard")


    }


    finally{


        loading.value=false


    }


}



onMounted(loadDashboard)



</script>

<template>


<div class="student-layout">



    <!-- Sidebar -->


    <StudentSidebar />




    <div class="student-content">



        <!-- Navbar -->


        <StudentNavbar />





        <div class="container-fluid mt-4">



            <!-- Header -->


            <StudentPageHeader

                title="Student Dashboard"

                subtitle="Track your placement journey and opportunities"

            />







            <!-- Loading -->


            <StudentLoading

                v-if="loading"

            />








            <template v-else>





                <!-- Statistics Cards -->


                <div class="row g-4 mb-4">



                    <div


                        class="col-md-3"


                        v-for="card in cards"


                        :key="card.title"


                    >



                        <StudentStatsCard


                            :title="card.title"


                            :value="card.value"


                            :icon="card.icon"


                        />



                    </div>



                </div>









                <!-- Profile Progress -->


                <div class="row g-4 mb-4">



                    <div class="col-md-6">



                        <StudentProgressCard


                            title="Profile Completion"


                            :value="dashboard.profile_completion"


                            message="Complete your profile to improve your chances."


                        />



                    </div>





                    <div class="col-md-6">



                        <StudentSectionCard

                            title="Placement Status"

                        >



                            <h4 class="text-success">


                                {{ dashboard.selected }}

                                Offers Received 🎉


                            </h4>



                            <p class="text-muted">


                                Keep applying for more opportunities.


                            </p>



                        </StudentSectionCard>



                    </div>



                </div>









                <!-- Recent Applications -->


                <StudentTableCard


                    title="Recent Applications"


                >




                    <table

                        class="table table-hover"

                        v-if="dashboard.recent_applications.length"

                    >



                        <thead>


                            <tr>


                                <th>

                                    Company

                                </th>


                                <th>

                                    Role

                                </th>


                                <th>

                                    Status

                                </th>


                                <th>

                                    Date

                                </th>



                            </tr>


                        </thead>





                        <tbody>



                            <tr


                                v-for="item in dashboard.recent_applications"


                                :key="item.id"


                            >



                                <td>

                                    {{ item.company }}

                                </td>




                                <td>

                                    {{ item.role }}

                                </td>





                                <td>


                                    <span

                                        class="badge bg-primary"

                                    >

                                        {{ item.status }}

                                    </span>


                                </td>





                                <td>

                                    {{ item.date }}

                                </td>



                            </tr>



                        </tbody>



                    </table>







                    <StudentEmptyState


                        v-else


                        title="No Applications"


                        message="You have not applied for any drives yet."


                        icon="bi bi-file-earmark-text"


                    />




                </StudentTableCard>





            </template>





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

    margin-left:0;

    padding:0;


}



.container-fluid{


    padding:25px;


}





.badge{


    padding:8px 14px;

    border-radius:20px;

    font-size:13px;


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



}




</style>