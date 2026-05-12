## The Analog Kid — Image Definitions

## Click-to-continue bounce indicator
image ctc:
    Text("▼", color="#aaaaaa", size=18)
    block:
        yoffset 0
        linear 0.4 yoffset 7
        linear 0.4 yoffset 0
        repeat
## All images registered here. Scene statements use these names.

## 1955 Backgrounds
image bg_main_street_1955       = "images/locations/1955/main_street.png"
image bg_beaumont_practice_1955 = "images/locations/1955/beaumont_practice.png"
image bg_hospital_north_1955    = "images/locations/1955/hospital_north.png"
image bg_ihs_clinic_1955        = "images/locations/1955/ihs_clinic.png"
image bg_tracks_crossing_1955   = "images/locations/1955/tracks_crossing.png"

## SVG sketches — convert with: magick -background "#F5F0E8" input.svg output.png
image bg_earls_diner_1955       = "images/locations/1955/earls_diner_1955.png"
image bg_first_baptist_1955     = "images/locations/1955/first_baptist_1955.png"
image bg_geri_office_1955       = "images/locations/1955/geri_office_1955.png"
image bg_frank_office_1955      = "images/locations/1955/frank_office_1955.png"
image bg_city_hall_1955         = "images/locations/1955/city_hall_1955.png"
image bg_vfw_hall_1955          = "images/locations/1955/vfw_hall_1955.png"
image bg_town_square_1955       = "images/locations/1955/town_square_1955.png"
image bg_tribal_office_1955     = "images/locations/1955/tribal_office_1955.png"
image bg_holloway_derrick_1955  = "images/locations/1955/holloway_derrick_1955.png"
image bg_barbershop_1955        = "images/locations/1955/barbershop_1955.png"
image bg_waiting_room_1955      = "images/locations/1955/1955-waiting-room-00.png"

## Solid placeholders (no SVG yet)
image bg_library_1955           = Solid("#0d1420")
image bg_south_side_street_1955 = Solid("#0d140d")

## Add more periods here as images are generated:
## image bg_main_street_1967 = "images/locations/1967/main_street.png"
## etc.
