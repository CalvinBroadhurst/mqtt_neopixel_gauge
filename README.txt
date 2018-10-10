
Read connect to mqtt_server, as mqtt_client, and subscribe to mqtt_topic
When a new numeric value is published in the topic, update the neopixel display to show it's value
Value is represented by the number of pixels and the colour of the pixels

"neopixel_pin" = the pin the neopixel display is connected to
"pixels" = the number of pixels to use (there must be the same number of entries in "leds" as this
"colours" = r, g, b values to be used for the pixels
"leds" = the value at which each pixel starts (uses >= comparison) and the colour to use for each
"max" = if this is reached then set all pixels to the specified colour

config.json
{
	"mqtt_server" : "broker.mqttdashboard.com",
	"mqtt_client" : "clientname",
	"mqtt_topic" : "topic/topic",
	"neopixel_pin" : 14,
	"pixel_count" : 24
	"colours" : {
				"blue" : [0, 0, 32],
				"green" : [0, 32, 0],
				"yellow" : [32, 32, 0]
				"orange" : [32, 16, 0]
				"red" : [32, 0, 0]
				},
	"pixels" : [ 
			   { "min_val" : 0.0, "colour" : "blue" },
			   { "min_val" : 2.0, "colour" : "blue" },
			   { "min_val" : 4.0, "colour" : "blue" },
			   { "min_val" : 6.0, "colour" : "blue" },
			   { "min_val" : 8.0, "colour" : "blue" },
			   { "min_val" : 10.0, "colour" : "green" },
			   { "min_val" : 12.0, "colour" : "green" },
			   { "min_val" : 14.0, "colour" : "green" },
			   { "min_val" : 16.0, "colour" : "green" },
			   { "min_val" : 18.0, "colour" : "green" },
			   { "min_val" : 20.0, "colour" : "yellow" },
			   { "min_val" : 22.0, "colour" : "yellow" },
			   { "min_val" : 24.0, "colour" : "yellow" },
			   { "min_val" : 26.0, "colour" : "yellow" },
			   { "min_val" : 28.0, "colour" : "yellow" }
			   { "min_val" : 30.0, "colour" : "orange" }
			   { "min_val" : 32.0, "colour" : "orange" }
			   { "min_val" : 34.0, "colour" : "orange" }
			   { "min_val" : 36.0, "colour" : "orange" }
			   { "min_val" : 38.0, "colour" : "orange" }
			   { "min_val" : 40.0, "colour" : "red" }
			   { "min_val" : 42.0, "colour" : "red" }
			   { "min_val" : 44.0, "colour" : "red" }
			   { "min_val" : 46.0, "colour" : "red" }
			 ],
	"max" : { "max_value" : 50, "colour" : "red" }
}