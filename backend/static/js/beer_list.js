

const EventHandling = {
    delimiters: ["${", "}"],
    items: [],
    data() {
        return {
            count: null,
            items: null
        }
    },
    methods: {
        loadMore() {
            console.log('fetching more beers');
        }
    },
    mounted() {
        fetch('http://127.0.0.1:8000/api/beers/')
            .then((response) => {
                response.json()
                    .then( data => {
                        console.log(data);
                        this.items = data.results;
                        this.count = data.count;
                    });
            });
    }
}

Vue.createApp(EventHandling).mount('#beer_list')
