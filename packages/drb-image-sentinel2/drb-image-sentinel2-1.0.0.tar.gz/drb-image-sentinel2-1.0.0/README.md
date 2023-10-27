# DRB Sentinel-2 Image AddOn

This addon enrich the `Sentinel-2 Product` topics with a preview image extractor.

## Available Images
|Product|Image name|Path|
|-------|----------|----|
|Level-1C|preview|GRANULE/*/QI_DATA/*_PVI.jp2|
|Level-1C|TrueColorImage|GRANULE/*/IMG_DATA/*_TCI*.jp2|
|Level-1C|{band_name}]|GRANULE/*/IMG_DATA/{band_name}|
|Level-2A|preview|GRANULE/*/QI_DATA/*_PVI.jp2|
|Level-2A|TrueColorImage|GRANULE/*/IMG_DATA/*_TCI*.jp2|
|Level-2A|{band_name}|GRANULE/*/IMG_DATA/*/{band_name}|

{band_name} correspond to the name of the actual .jp2 file

## Example
```python
zip_node = resolver.create('/path/to/sentinel2.zip')
safe_node = zip_node[0]
# Retrieve the addon image object corresponding to the product (preview by default)
image = AddonImage.apply(safe_node)
# The image name can be specified
image = AddonImage.apply(safe_node, image_name='preview')
# Retrieve the drb-driver-image node corresponding to the addon using the default extraction
addon_image_node = image.image_node()
# Retrieve the rasterio implementation of the default image
dataset = image.get_impl(rasterio.DatasetReader) 
```