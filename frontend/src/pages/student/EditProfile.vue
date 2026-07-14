<script setup>

import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"

import StudentSidebar from "../../components/student/StudentSidebar.vue"
import StudentNavbar from "../../components/student/StudentNavbar.vue"
import StudentPageHeader from "../../components/student/StudentPageHeader.vue"
import StudentSectionCard from "../../components/student/StudentSectionCard.vue"
import StudentLoading from "../../components/student/StudentLoading.vue"

import {

    getProfile,

    updateProfile

} from "../../services/student"



const router = useRouter()

const loading = ref(true)

const saving = ref(false)



const student = ref({

    full_name:"",

    phone:"",

    address:"",

    course:"",

    branch:"",

    cgpa:"",

    graduation_year:"",

    year:"",

    tenth_marks:"",

    twelfth_marks:"",

    skills:"",

    dob:""

})



async function loadProfile(){

    try{

        const response = await getProfile()

        student.value = {

            ...response

        }

    }

    catch(error){

        console.error(error)

        alert("Unable to load profile")

    }

    finally{

        loading.value = false

    }

}



async function saveProfile(){

    saving.value = true

    try{

        await updateProfile(student.value)

        alert("Profile updated successfully")

        router.push("/student/profile")

    }

    catch(error){

        console.error(error)

        alert("Unable to update profile")

    }

    finally{

        saving.value = false

    }

}



onMounted(loadProfile)

</script>

<template>

<div class="student-layout">

    <StudentSidebar />

    <div class="student-content">

        <StudentNavbar />

        <div class="container-fluid mt-4">

            <StudentPageHeader

                title="Edit Profile"

                subtitle="Update your academic and personal information"

            />



            <StudentLoading

                v-if="loading"

            />



            <template v-else>

                <StudentSectionCard

                    title="Student Information"

                >

                    <form @submit.prevent="saveProfile">

                        <div class="row g-4">

                            <div class="col-md-6">

                                <label class="form-label">

                                    Full Name

                                </label>

                                <input

                                    type="text"

                                    class="form-control"

                                    v-model="student.full_name"

                                >

                            </div>



                            <div class="col-md-6">

                                <label class="form-label">

                                    Phone

                                </label>

                                <input

                                    type="text"

                                    class="form-control"

                                    v-model="student.phone"

                                >

                            </div>



                            <div class="col-md-6">

                                <label class="form-label">

                                    Course

                                </label>

                                <input

                                    type="text"

                                    class="form-control"

                                    v-model="student.course"

                                >

                            </div>



                            <div class="col-md-6">

                                <label class="form-label">

                                    Branch

                                </label>

                                <input

                                    type="text"

                                    class="form-control"

                                    v-model="student.branch"

                                >

                            </div>



                            <div class="col-md-6">

                                <label class="form-label">

                                    CGPA

                                </label>

                                <input

                                    type="number"

                                    step="0.01"

                                    class="form-control"

                                    v-model="student.cgpa"

                                >

                            </div>



                            <div class="col-md-6">

                                <label class="form-label">

                                    Graduation Year

                                </label>

                                <input

                                    type="number"

                                    class="form-control"

                                    v-model="student.graduation_year"

                                >

                            </div>



                            <div class="col-md-6">

                                <label class="form-label">

                                    Current Year

                                </label>

                                <input

                                    type="number"

                                    class="form-control"

                                    v-model="student.year"

                                >

                            </div>



                            <div class="col-md-6">

                                <label class="form-label">

                                    Date of Birth

                                </label>

                                <input

                                    type="date"

                                    class="form-control"

                                    v-model="student.dob"

                                >

                            </div>



                            <div class="col-md-6">

                                <label class="form-label">

                                    10th Marks

                                </label>

                                <input

                                    type="number"

                                    step="0.01"

                                    class="form-control"

                                    v-model="student.tenth_marks"

                                >

                            </div>



                            <div class="col-md-6">

                                <label class="form-label">

                                    12th Marks

                                </label>

                                <input

                                    type="number"

                                    step="0.01"

                                    class="form-control"

                                    v-model="student.twelfth_marks"

                                >

                            </div>



                            <div class="col-12">

                                <label class="form-label">

                                    Address

                                </label>

                                <textarea

                                    rows="3"

                                    class="form-control"

                                    v-model="student.address"

                                ></textarea>

                            </div>



                            <div class="col-12">

                                <label class="form-label">

                                    Skills

                                </label>

                                <textarea

                                    rows="4"

                                    class="form-control"

                                    v-model="student.skills"

                                ></textarea>

                            </div>

                        </div>



                        <div class="d-flex justify-content-end gap-3 mt-4">

                            <RouterLink

                                to="/student/profile"

                                class="btn btn-outline-secondary"

                            >

                                Cancel

                            </RouterLink>



                            <button

                                type="submit"

                                class="btn btn-primary"

                                :disabled="saving"

                            >

                                <i class="bi bi-check-circle me-2"></i>

                                {{ saving ? "Saving..." : "Save Changes" }}

                            </button>

                        </div>

                    </form>

                </StudentSectionCard>

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

}



.container-fluid{

    padding:25px;

}



.form-label{

    font-weight:600;

    color:#334155;

    margin-bottom:8px;

}



.form-control{

    border-radius:12px;

    border:1px solid #CBD5E1;

    padding:12px 15px;

    transition:.25s;

}



.form-control:focus{

    border-color:#0EA5E9;

    box-shadow:0 0 0 .2rem rgba(14,165,233,.15);

}



textarea{

    resize:vertical;

}



.btn{

    border-radius:12px;

    padding:10px 22px;

    font-weight:600;

}



.btn i{

    font-size:15px;

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



    .d-flex{

        flex-direction:column;

    }



    .btn{

        width:100%;

    }

}

</style>