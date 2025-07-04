from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Location(BaseModel):
    name: str
    region: str
    country: str
    lat: float
    lon: float
    tz_id: str
    localtime_epoch: int
    localtime: str


class Condition(BaseModel):
    text: str
    icon: str
    code: int


class Current(BaseModel):
    last_updated_epoch: int
    last_updated: str
    temp_c: float
    temp_f: float
    is_day: int
    condition: Condition
    wind_mph: float
    wind_kph: float
    wind_degree: int
    wind_dir: str
    pressure_mb: int
    pressure_in: float
    precip_mm: int
    precip_in: int
    humidity: int
    cloud: int
    feelslike_c: float
    feelslike_f: float
    windchill_c: float
    windchill_f: float
    heatindex_c: float
    heatindex_f: float
    dewpoint_c: float
    dewpoint_f: float
    vis_km: int
    vis_miles: int
    uv: float
    gust_mph: float
    gust_kph: float


class Condition1(BaseModel):
    text: str
    icon: str
    code: int


class Day(BaseModel):
    maxtemp_c: float
    maxtemp_f: float
    mintemp_c: float
    mintemp_f: float
    avgtemp_c: float
    avgtemp_f: float
    maxwind_mph: float
    maxwind_kph: float
    totalprecip_mm: int
    totalprecip_in: int
    totalsnow_cm: int
    avgvis_km: int
    avgvis_miles: int
    avghumidity: int
    daily_will_it_rain: int
    daily_chance_of_rain: int
    daily_will_it_snow: int
    daily_chance_of_snow: int
    condition: Condition1
    uv: float


class Astro(BaseModel):
    sunrise: str
    sunset: str
    moonrise: str
    moonset: str
    moon_phase: str
    moon_illumination: int
    is_moon_up: int
    is_sun_up: int


class Condition2(BaseModel):
    text: str
    icon: str
    code: int


class HourItem(BaseModel):
    time_epoch: int
    time: str
    temp_c: float
    temp_f: float
    is_day: int
    condition: Condition2
    wind_mph: float
    wind_kph: float
    wind_degree: int
    wind_dir: str
    pressure_mb: int
    pressure_in: float
    precip_mm: int
    precip_in: int
    snow_cm: int
    humidity: int
    cloud: int
    feelslike_c: float
    feelslike_f: float
    windchill_c: float
    windchill_f: float
    heatindex_c: float
    heatindex_f: float
    dewpoint_c: float
    dewpoint_f: float
    will_it_rain: int
    chance_of_rain: int
    will_it_snow: int
    chance_of_snow: int
    vis_km: int
    vis_miles: int
    gust_mph: float
    gust_kph: float
    uv: float


class ForecastdayItem(BaseModel):
    date: str
    date_epoch: int
    day: Day
    astro: Astro
    hour: List[HourItem]


class Forecast(BaseModel):
    forecastday: List[ForecastdayItem]


class WeatherForecast(BaseModel):
    location: Location
    current: Current
    forecast: Forecast
