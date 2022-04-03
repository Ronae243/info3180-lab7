<template>
    
    <div>
        <form @submit.prevent="uploadPhoto" id="uploadForm">
            <div>
                <textarea name="description" id="description"></textarea>
            </div>  

             <div>
                <input type="file" id="up_image" name="up_image">
            </div>
  

            <div>
                <button class="b">Submit</button>
            </div>    
            
             
        </form>   
    </div>
   
</template>

<script>
export default{
    data(){
        return{};
    },
    methods:{
        uploadPhoto(){
            fetch("/api/upload", {
            method: 'POST',
            })

            .then(function (response) {
            return response.json();
            })
            .then(function (data) {
            console.log(data);
            })
            .catch(function (error) {
            console.log(error);
            });
        },
    }
}
</script>