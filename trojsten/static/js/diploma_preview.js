(function($)
{
    $(function()
    {
        let fields = JSON.parse(template_fields.replace(/&quot;/g,'"'));

        function refresh_form() {
            var current_fields = fields[document.getElementById("id_template").value];

            var container = document.getElementById("dummy_form");
            while (container.firstChild) {
                container.removeChild(container.firstChild);
            }

            $.each(current_fields, function (index, field_name) {
                var input = document.createElement("input");
                input.setAttribute("type", "text");
                input.setAttribute('id', 'id_' + field_name);
                input.setAttribute("name", field_name);
                input.setAttribute("value", "");
                var label = document.createElement('label');
                label.setAttribute('for', 'id_' + field_name);
                label.innerHTML = field_name;
                var input_container = document.createElement("div");
                input_container.className = "form-group";
                input_container.appendChild(label);
                input_container.appendChild(input);
                document.getElementById("dummy_form").appendChild(input_container);
            })
        }

        function serialize_data(){
            let d = {};
            document.getElementById("dummy_form").childNodes.forEach(function(item){
                d[item.childNodes[1].name] = item.childNodes[1].value;
            });
            return JSON.stringify([d]);
        }

        $(document).ready(function(){
            refresh_form()
        });

        $("#form").on({
            submit: function(){
                document.getElementById("id_single_participant_data").value = serialize_data();
            }
        });

        $("#id_template").on({
            change: function () {
                refresh_form();
                serialize_data();
            }
        });

    });
})(jQuery);