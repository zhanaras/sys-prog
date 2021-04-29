export interface days {
    date: string,
    min_temp: number,
    max_temp: number,
    feels_like: number,
    day: Text,
    night: Text
}

export interface hours {
    date: string,
    temp: number,
    feels_like: number,
    uv: number,
    uv_text: string,
    humidity: number,
    wind_speed: number,
    wind_speed_unit: string,
    desc: Text,
    prec: boolean,
    daylight: boolean,
    prec_prob: number
}

export interface city{
    city_name: string
}
