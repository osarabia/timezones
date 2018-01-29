var app = new Vue({
    el: '#app',
    data: function(){
        var vm = {
            city: "",
            city_id: 0,
            choosen: false,
            cities: [],
            watchlist: []
        };


        axios.get("/watchlist/")
             .then(function(resp) {
                 vm.watchlist = resp.data;
             })
             .catch(function(e) {
                 console.log(e);
             });

        return vm;
    },
    computed:{
        isNotEmptyCities: function(){
            if(this.cities.length === 0){
                return false;
            }

            return true;
        },
        notEmptyCity: function(){
            if(this.city_id === 0){
                return true;
            }

            return false;
        }
    },
    watch:{
        city: function(newCity, oldCity) {
            if(newCity.length === 0){
                this.cities = [];

                return
            }

            if(this.choosen) {
                this.choosen = false;

                return
            }

            this.getCities(newCity);
        }
    },
    methods: {
        setCity: function(city){
            this.city_id = city.id;
            this.choosen = true;
            this.city = city.country+", "+city.name;
            this.cities = [];
        },
        addToWatchList: function(){
            resource = "/watchlist/";

            var vm = this;
            var d = new Date();
            var payload = { 
                              "city_id": this.city_id,
                              "timestamp": (d.getTime()-d.getMilliseconds())/1000
                          };
            axios.post(resource, payload)
                 .then(function(resp){
                     vm.watchlist.push(resp.data);
                     vm.city = "";
                     vm.city_id = 0;
                 })
                 .catch(function(e){
                     vm.city = "";
                     vm.city_id = 0;
                 });
        },
        getCities: _.debounce(function(city){
            filter_city = "/cities?startswith="+city;
            var vm = this;
            axios.get(filter_city)
                 .then(function(resp){
                     vm.cities = resp.data;
                 })
                 .catch(function(e){
                     vm.cities = [];
                 });
        }, 500),
        getWatchlist: function(){
            var vm = this;
            axios.get("/watchlist/")
                 .then(function(resp) {
                     vm.watchlist = resp.data;
                 })
                 .catch(function(e) {
                     console.log(e);
                 });
        },
        deleteCity: function(city_id) {
            resource = "watchlist/" + city_id;
            var vm = this;
            axios.delete(resource)
                .then(function() {
                    vm.getWatchlist();
                })
        }
    }
});
