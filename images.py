import pygame
import base64
import io

pygame.init()
pygame.display.set_mode()

img_bytes = b"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAHgSURBVFhHY2TAAt7IqPyHMrECkSd3sOpDBva3sreB6INqU73AAjgAE5SmKgi5V+1z/vstTxAGsaHCWAFNHHDs6+V1UCYKGxugugNMbiRd/fLvOyuUywBiw6IDG6CqA0DBfevnYy0oFw7wRQVVHbD78+nNUCYGwCVHNQeAgv4/A+7MA5IDqYFy4YAqDvC8U9yJLejRAUgNSC2UCwZUKQf4LrriVY8OPunvhuunOAQ0rkW+hjKJBspXQz9CmZQ5AJS9nv1+IwLlEg1e//nAB4sKihwAyl5QJsng6NdLZSCabAdIXfb7BWWSDUBmULUyIpQYkRMfDFAlG1ICRh0w6gDGt+r6v/5//Qqvv8kBjNzcv4VvXmQjKxeANELZZANKzABHAYueznYwjwzAamHWBWWSBeBB8s7E5vW/Fy9IKteZRIQ/CV04yQ/lUlYQCZ05IgplEg2QLScXoOQCUoKT0qCHARQH8K9ZVs6srHQNysUJQGpAaqFcigBGOSB4cJc2AyPWugYCgHJgNVQCGA4AAVZHO18oEwPgkyMHYHUA/6K5W7BFBSi7guSgXKoArA4AAVAwg0o4KBdc2gls24C3o0kOwOkAEGAxNwmCMlHY1AR4UhsEfPAKAPfriPE96QURAwMAKgSxtD/GsPoAAAAASUVORK5CYII="
flip_power = pygame.image.load(io.BytesIO(base64.b64decode(img_bytes))).convert_alpha()
img_bytes = b"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANdSURBVFhHtVa/TxRBFH6zHCRED4hI5V2huUILgUKLMyEx4YeS2N79AXbEUByWGgt6joRGGgoTK6iMCglQc4UNUBgjxMI7KkARjBiO7Pje3OxkZtnZnSXxSzbzdm5uv++9983sMnDE4Y1CiTNYlLdwvbEb+1+OkGEsPDkmwmdQkiGgkFkZxsFlDThX4CBXUBklZW8DFmUDh2LrrgWnCuznC1UZAqpYkmEqRJETnAQwDhUZgsehIUNnRJBPyTFZAJlPhgLY/wq2YyM8b0MUOWNM+SNRgG4+DUXaEbovopBETkgUgG5TAjzOJmSogJVQ7dHhQk6IFaCXmcx3bW9nnnaAbkSsRBXXGeZyJSfECtAPHjSfIu1r7JZxUGbEdUQokIJcGNEqIGyy3r1dY/thGYysaX2azGkeL2YVYJx8EXsfBRnbkfX1vsXBiVyHVYBpvujDB6uQlyH4B4cdZx9W5J0bOSFSQNh84fIHoCq0Pxw6pHj/0T1YHroCb34sz7mSEyLPdDpocBDlxCzLNgF6z7u3x2hogfPZ48F1ddrF4UIFZPaqly7khKte55EMUTWrZDdHLycgyXyEKLf/9Jt38QtArWcMZrq2Rr/LWysuCEgyn22rnQ6sNE4G18r4APXmRORRBOZhhyEgyXwu+/y4f+05pm+Uv3NrPCdDA9nt4aIhQC9/OHsX8gDH/avGfDuc12UoxHRtjlSzWyN1xr0NtQvESWb55ktDHoCIAmLqAT5smgN/yoAZ1VAViDIfEufwooekIieQJ2QY7PVXYXIU1FACwuYjcgxreOl/SiSnvuIWXIwzH+0WzvwHJwPreSEuVP5Gb32HMnYmF+XmzSl8RimcpYavuDVf/upfM7wlBOznCotBBTJ3bk90r75/gWEsOZF2sPOiz3nVRkolxvddtcnblvSW6GCYfQ6VK5di9rTQSt69PVryfcxU84wOIsUPhNo5y0zZSHUwPfu2seHTnoX5TvFLC4Kc+gq+V7GREqivngdL4RIngekfltnXc9DxZFzEn/58mR7ZmczG95XVGOOzZzxTc8k2CoaAv99qSPwZntVnjn77pz1y2oBLX9NACXg3eR8qjw/EZBhp+5oGSsCtjzfFhI7L9jUNxEFEXzIBWiWGchMyeXq7/U9yAIB/9DuyUcfMJFMAAAAASUVORK5CYII="
angle_power = pygame.image.load(io.BytesIO(base64.b64decode(img_bytes))).convert_alpha()
img_bytes = b"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGBSURBVFhHxZXNUcMwEIVtUgIMp+QGRVBIuqEGCkkjNMEtOZIa4D1ppdHP2pIlO/5mdiSW9b7V6ifj0MEfkGkzTzIuBtpnmXbR24ErhqP9q43eAij+AfsyDp0D7FXGjEUF/B7fsj1/uf1M5pACv2GTXWruQFiMVkSNOMk+TFepJS/FFMTvsGc7VW4Bk821tXPlN9innVrUa0iR0sobxXlg2QFPVsCW4uM4cpwmFAmh35m4IigOu8I06PdFYX42XsF3gMn3WLkvYK+2q4cwZbM9b4XisKo9T8H/ojMg7nrwTbO4AzEXEw2y1s6B+NXajlzLfs4pDutaeRF318PTT5hcRDTWEXekBTC5iGh0i0dngMK8cm6U5Oqe30/vMotJr2zaTaJd6yyQ4rJCjWjl/NaZuFS0OPMQ0RFWJcmrTntJ1DEVZwpYQ1xtqzAXFz3FjxYnvoA9xIlx7iVOZq8a2FSccAuqxEPWEjegAxrNLxwLCIsoYvUiup/XRVhNz2PFh2H4B//UdWjr1g1uAAAAAElFTkSuQmCC"
speed_power = pygame.image.load(io.BytesIO(base64.b64decode(img_bytes))).convert_alpha()

power_images = {
    "flip": flip_power,
    "angle": angle_power,
    "speed": speed_power
}

pygame.display.quit()