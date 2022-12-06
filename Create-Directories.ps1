$rootDir = "C:\Users\jon\source\repos\AdventOfCode\AdventOfCode\2022"
$start = 1
$max = 25

do {

$newDir = Join-Path -Path $rootDir -ChildPath $("Day" + $i)
$dayOneDir = Join-Path -Path $newDir -ChildPath "P1"
$dayTwoDir = Join-Path -Path $newDir -ChildPath "P2"

New-Item -Path $newDir -ItemType Directory
New-Item -Path $dayOneDir -ItemType Directory
New-Item -Path $dayTwoDir -ItemType Directory

$i++

} while ($i -le $max)