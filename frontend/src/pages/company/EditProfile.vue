<script setup>

import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"

import CompanySidebar from "../../components/company/CompanySidebar.vue"
import CompanyNavbar from "../../components/company/CompanyNavbar.vue"
import CompanyPageHeader from "../../components/company/CompanyPageHeader.vue"
import CompanySectionCard from "../../components/company/CompanySectionCard.vue"
import CompanyLoading from "../../components/company/CompanyLoading.vue"

import {

    getProfile,
    updateCompanyProfile

} from "../../services/auth"



const router = useRouter()

const loading = ref(true)

const saving = ref(false)



const company = ref({

    company_name:"",

    industry:"",

    website:"",

    location:"",

    hr_name:"",

    hr_email:"",

    hr_phone:"",

    description:""

})



async function loadProfile(){

    loading.value = true

    try{

        const response = await getProfile()

        if(response.profile){

            company.value = {

                ...response.profile

            }

        }

    }

    catch(error){

        console.error(error)

        alert("Unable to load profile.")

    }

    finally{

        loading.value = false

    }

}



async function saveProfile(){

    saving.value = true

    try{

        await updateCompanyProfile(

            company.value

        )



        alert(

            "Profile updated successfully."

        )



        router.push(

            "/company/profile"

        )

    }

    catch(error){

        console.error(error)

        alert(

            "Unable to update profile."

        )

    }

    finally{

        saving.value = false

    }

}



onMounted(

    loadProfile

)

</script>
<template>

<div class="company-layout">


    <CompanySidebar />


    <div class="company-content">


        <CompanyNavbar />


        <div class="container-fluid mt-4">


            <CompanyPageHeader

                title="Edit Company Profile"

                subtitle="Update your organization information"

            />



            <CompanyLoading

                v-if="loading"

            />



            <CompanySectionCard

                v-else

                title="Company Information"

            >



            <form @submit.prevent="saveProfile">



                <div class="row g-4">



                    <!-- Company Name -->

                    <div class="col-md-6">

                        <label>

                            Company Name

                        </label>


                        <input

                            type="text"

                            class="form-control"

                            v-model="company.company_name"

                            required

                        >

                    </div>




                    <!-- Industry -->

                    <div class="col-md-6">


                        <label>

                            Industry

                        </label>


                        <input

                            type="text"

                            class="form-control"

                            v-model="company.industry"

                        >


                    </div>




                    <!-- Website -->

                    <div class="col-md-6">


                        <label>

                            Website

                        </label>


                        <input

                            type="text"

                            class="form-control"

                            v-model="company.website"

                        >


                    </div>





                    <!-- Location -->

                    <div class="col-md-6">


                        <label>

                            Location

                        </label>


                        <input

                            type="text"

                            class="form-control"

                            v-model="company.location"

                        >


                    </div>





                    <!-- HR Name -->

                    <div class="col-md-6">


                        <label>

                            HR Name

                        </label>


                        <input

                            type="text"

                            class="form-control"

                            v-model="company.hr_name"

                        >


                    </div>





                    <!-- HR Email -->

                    <div class="col-md-6">


                        <label>

                            HR Email

                        </label>


                        <input

                            type="email"

                            class="form-control"

                            v-model="company.hr_email"

                        >


                    </div>





                    <!-- HR Phone -->

                    <div class="col-md-6">


                        <label>

                            HR Phone

                        </label>


                        <input

                            type="text"

                            class="form-control"

                            v-model="company.hr_phone"

                        >


                    </div>






                    <!-- Description -->

                    <div class="col-12">


                        <label>

                            Company Description

                        </label>


                        <textarea

                            rows="5"

                            class="form-control"

                            v-model="company.description"

                        ></textarea>


                    </div>




                </div>





                <div class="mt-4">


                    <button

                        type="submit"

                        class="btn btn-success w-100"

                        :disabled="saving"

                    >


                        <span v-if="saving">

                            Saving...

                        </span>


                        <span v-else>


                            <i class="bi bi-save me-2"></i>

                            Save Changes


                        </span>


                    </button>


                </div>



            </form>




            </CompanySectionCard>



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



label{

    font-weight:600;

    color:#334155;

    margin-bottom:8px;

    display:block;

}



.form-control{

    border-radius:12px;

    padding:12px 15px;

    border:1px solid #CBD5E1;

    transition:.25s;

}



.form-control:focus{

    border-color:#16A34A;

    box-shadow:0 0 0 .2rem rgba(22,163,74,.15);

}



textarea{

    resize:none;

}



.btn-success{

    background:#16A34A;

    border:none;

    padding:13px;

    border-radius:12px;

    font-weight:600;

    transition:.25s;

}



.btn-success:hover{

    background:#15803D;

}



.btn-success:disabled{

    opacity:.7;

    cursor:not-allowed;

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

}

</style>