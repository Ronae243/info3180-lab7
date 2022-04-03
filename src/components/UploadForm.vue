<template>
    
    <div class="grid">
        <form @submit.prevent="uploadPhoto" id="uploadForm">
            <div class="rowa">
                <p id="atxt">Description</p>
                <textarea name="description" id="description"></textarea>
            </div>  

             <div>
                <p id="atxt">Photo Upload</p> 
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
        return{
            csrf_token: ''
        };
    },
    created() {
        this.getCsrfToken();
    },
    methods:{
        uploadPhoto(){
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);
            fetch("/api/upload", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRFToken': this.csrf_token
                }
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
        getCsrfToken() {
            let self = this;
                fetch('/api/csrf-token')
                    .then((response) => response.json())
                    .then((data) => {
                        console.log(data);
                        self.csrf_token = data.csrf_token;
                    })
        }
    }
}
</script>

<style>
body{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
#description{
    width: 100%;
    margin-bottom: 10px;
}

.grid{
    display: grid;
}

p{
    font-weight: 500;
}

button{
    margin-top: 20px;
    box-shadow: none;
    border: none;
    border-radius: 5px;
    height: 40px;
    width: 80px;
    background: rgb(0,123,255);
    color: white;
}

#atxt{
    margin-bottom: 8px;
}

.rowa{
    margin-top: 20px;
}
</style>