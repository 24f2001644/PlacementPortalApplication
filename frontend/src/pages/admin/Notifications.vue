<script setup>

import { ref, onMounted } from "vue"

import AdminSidebar from "../../components/admin/AdminSidebar.vue"
import AdminNavbar from "../../components/admin/AdminNavbar.vue"
import AdminPageHeader from "../../components/admin/AdminPageHeader.vue"
import AdminSectionCard from "../../components/admin/AdminSectionCard.vue"
import AdminEmptyState from "../../components/admin/AdminEmptyState.vue"

import {
    getNotifications,
    createNotification
} from "../../services/admin"


const message = ref("")

const notifications = ref([])

const loading = ref(false)



async function loadNotifications(){

    try{

        notifications.value = await getNotifications()

    }

    catch(error){

        console.error(error)

    }

}



async function send(){


    if(!message.value.trim())

        return



    try{


        const response = await createNotification({

            message:message.value

        })


        notifications.value.unshift(response)



        message.value=""


    }

    catch(error){

        console.error(error)

        alert("Unable to send notification")

    }


}



onMounted(loadNotifications)


</script>



<template>


<div class="admin-layout">


    <AdminSidebar />


    <div class="admin-content">


        <AdminNavbar />



        <div class="container-fluid mt-4">



            <AdminPageHeader

                title="Notifications"

                subtitle="Send updates to students and companies"

            />





            <div class="row g-4">



                <!-- Send Notification -->


                <div class="col-md-5">


                    <AdminSectionCard

                        title="Create Notification"

                    >


                        <textarea

                            class="form-control"

                            rows="6"

                            placeholder="Write notification..."

                            v-model="message"

                        ></textarea>



                        <button

                            class="btn btn-primary mt-3 w-100"

                            @click="send"

                        >

                            <i class="bi bi-send me-2"></i>

                            Send Notification


                        </button>



                    </AdminSectionCard>



                </div>






                <!-- Notification History -->


                <div class="col-md-7">



                    <AdminSectionCard

                        title="Notification History"

                    >



                    <ul

                        class="list-group"

                        v-if="notifications.length"

                    >


                        <li

                            class="list-group-item"

                            v-for="item in notifications"

                            :key="item.id"

                        >



                            <div class="d-flex justify-content-between">


                                <strong>

                                    {{ item.date }}

                                </strong>



                            </div>



                            <p class="mb-0 mt-2">

                                {{ item.message }}

                            </p>



                        </li>



                    </ul>



                    <AdminEmptyState

                        v-else

                        message="No notifications sent yet"

                    />



                    </AdminSectionCard>



                </div>




            </div>



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



.container-fluid{

    padding:25px;

}



</style>