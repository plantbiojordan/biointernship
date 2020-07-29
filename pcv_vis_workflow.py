#!/usr/bin/env python
# coding: utf-8

# In[1]:


from plantcv import plantcv as pcv


# In[ ]:


# This command outputs all resulting images to the notebook.
pcv.params.debug='plot'


# In[6]:


# Importing the image. Including the path was necessary. Mode="native" by default.
img, path, img_filename = pcv.readimage(filename="/users/jordanmanchengo/data/duckweed1.png")


# In[11]:


# Hue channel.
h = pcv.rgb2gray_hsv(rgb_img=img, channel='h')


# In[12]:


# Saturation channel.
s = pcv.rgb2gray_hsv(rgb_img=img, channel='s')


# In[13]:


# Value channel.
v = pcv.rgb2gray_hsv(rgb_img=img, channel='v')


# In[14]:


# Setting a saturation threshold on "light" objects to create sharp contrast.
s_thresh = pcv.threshold.binary(gray_img=s, threshold=85, max_value=255, object_type='light')


# In[20]:


# Using a median blur to reduce background noise
s_mblur = pcv.median_blur(gray_img=s_thresh, ksize=5)


# In[21]:


# Same as line above.
s_cnt = pcv.median_blur(gray_img=s_thresh, ksize=5)


# In[15]:


# Converting RGB image to LAB image and extracting the blue channel.
b = pcv.rgb2gray_lab(rgb_img=img, channel='b')


# In[16]:


# Establishing a threshold in the blue channel image.
b_thresh = pcv.threshold.binary(gray_img=b, threshold=160, max_value=255, 
                                object_type='light')


# In[17]:


# Same as line above.
b_cnt = pcv.threshold.binary(gray_img=b, threshold=160, max_value=255, 
                                object_type='light')


# In[18]:


# Optional step in vis workflow that I tried. Fills small objects, not very useful here.
b_fill = pcv.fill(b_thresh, 10)


# In[22]:


# Joining the s_mblur image with the b_cnt image.
bs = pcv.logical_or(bin_img1=s_mblur, bin_img2=b_cnt)


# In[24]:


# The image above is now used as a "mask" over the original image to wipe the background.
masked = pcv.apply_mask(img=img, mask=bs, mask_color='white')


# In[25]:


# Extracting the Green-Magenta channel.
masked_a = pcv.rgb2gray_lab(rgb_img=masked, channel='a')


# In[26]:


# Extracting the Blue-Yellow channel.
masked_b = pcv.rgb2gray_lab(rgb_img=masked, channel='b')


# In[27]:


# Thresholding the Green-Magenta channel using "dark".
maskeda_thresh = pcv.threshold.binary(gray_img=masked_a, threshold=115, 
                                      max_value=255, object_type='dark')


# In[28]:


# Thresholding the Green-Magenta channel using "light".
maskeda_thresh1 = pcv.threshold.binary(gray_img=masked_a, threshold=135, 
                                           max_value=255, object_type='light')


# In[29]:


# Thresholding the Blue-Yellow channel using "light".
maskedb_thresh = pcv.threshold.binary(gray_img=masked_b, threshold=128, 
                                          max_value=255, object_type='light')


# In[30]:


# Joining the thresholded saturation with the Blue-Yellow images.
ab1 = pcv.logical_or(bin_img1=maskeda_thresh, bin_img2=maskedb_thresh)


# In[31]:


# Same as line above.
ab = pcv.logical_or(bin_img1=maskeda_thresh1, bin_img2=ab1)


# In[32]:


# Filling any small objects even though there were none visible in the last image.
ab_fill = pcv.fill(bin_img=ab, size=200)


# In[34]:


# Appying the new mask for a wiped background.
masked2 = pcv.apply_mask(img=masked, mask=ab_fill, mask_color='white')


# In[35]:


# Object is masked and filled. If wispy leaves were pictured, the spaces between the
# leaves would've been filled as well. That does not apply here.
id_objects, obj_hierarchy = pcv.find_objects(masked2, ab_fill)


# In[46]:


# Selecting a region of interest (roi). Defining (x,y) sets the location for 
# the TOP LEFT corner of the rectangle.
roi1, roi_hierarchy= pcv.roi.rectangle(img=masked2, x=110, y=40, h=200, w=190)


# In[47]:


# This function is useful for separating plant from backgroud if there are many spaces between leaves.
roi_objects, hierarchy3, kept_mask, obj_area = pcv.roi_objects(img=img, roi_contour=roi1, 
                                                                   roi_hierarchy=roi_hierarchy, 
                                                                   object_contour=id_objects, 
                                                                   obj_hierarchy=obj_hierarchy,
                                                                   roi_type='partial')


# In[48]:


# Outline (blue) of all combined objects.
obj, mask = pcv.object_composition(img=img, contours=roi_objects, hierarchy=hierarchy3)


# In[49]:


# Shape analysis.
shape_img = pcv.analyze_object(img=img, obj=obj, mask=mask)


# In[50]:


# Boundary line output.
boundary_img1 = pcv.analyze_bound_horizontal(img=img, obj=obj, mask=mask, 
                                                   line_position=1680)


# In[54]:


# Histogram of color analysis.
color_histogram = pcv.analyze_color(rgb_img=img, mask=kept_mask, hist_plot_type='all')


# In[55]:


# Pseudocolored image based on value channels. This one analyzes saturation but can be
# manipulated to analyze hue or value.
pseudocolored_img = pcv.visualize.pseudocolor(gray_img=s, mask=kept_mask, cmap='jet')

